//Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
//You must do it in place.
// m: row size, n: col size

#include<iostream>
#include<vector>
#include<chrono>
using namespace std;
using namespace std::chrono;


// Time Complexity: O(n)
void setRow(vector<vector<int>>& matrix, int n, int m, int row) {
    for(int i=0; i<m; i++) {
        if(matrix[row][i] != 0)
            matrix[row][i] = -1;
    }
}

// Time Complexity: O(m)
void setCol(vector<vector<int>>& matrix, int n, int m, int col) {
    for(int i=0; i<n; i++) {
        if(matrix[i][col] != 0)
            matrix[i][col] = -1;
    }
}

// Time Complexity: O(m*n*m) or O(m**3). In-detail:  (m*n)(n+m) + (m*n)
// Space Complexity: O(1) or in-place 
void setZerosBruteForce(vector<vector<int>>& matrix) {
    int row = matrix.size();
    int col = matrix[0].size();

    for(int i=0; i<row; i++) {                   // m
        for(int j=0; j<col; j++) {               // n
            if(matrix[i][j] == 0) {
                setRow(matrix, row, col, i);     // n
                setCol(matrix, row, col, j);     // m
            }
        }
    }

    for(int i=0; i<row; i++) {                   // m
        for(int j=0; j<col; j++) {               // n
            if(matrix[i][j] == -1)
                matrix[i][j] = 0;
        }
    }
}



// Time Complexity: O(n*m). In-detail: (n*m) + (n*m)
// Space Complexity: O(m) + (n). Making use of extra array of size row and col
void setZerosBetter(vector<vector<int>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    int row[m] = {0};
    int col[n] = {0};

    for(int i=0; i<m; i++) {
        for(int j=0; j<n; j++) {
            if(matrix[i][j] == 0) {
                row[i] = 1;
                col[j] = 1;
            }
        }
    }

    for(int i=0; i<m; i++) {
        for(int j=0; j<n; j++) {
            if(row[i] || col[j])
                matrix[i][j] = 0;
        }
    }
}


void setZerosOptimized(vector<vector<int>>& matrix) {
    int m = matrix.size(), n = matrix[0].size();
    int col = 1;
    
    for(int i=0; i<m; i++) {
        for(int j=0; j<n; j++) {
            if(matrix[i][j] == 0) {
                matrix[i][0] = 0;
                if(j!=0)
                    matrix[0][j] = 0;
                else
                    col = 0;
            }
        }
    }

    for(int i=1; i<m; i++) {
        for(int j=1; j<n; j++) {
            if(matrix[i][0] == 0 || matrix[0][j] == 0)
                matrix[i][j] = 0;
        }
    }

    // first change the 1st row
    if(matrix[0][0] == 0) {
        for(int j=0; j<n; j++)
            matrix[0][j] = 0;
    }

    // now change the 1st col
    if(col == 0) {
        for(int i=0; i<m; i++)
            matrix[i][0] = 0;
    }
    
}






int main() {
    vector<vector<int>> matrix1 = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
    setZerosBruteForce(matrix1);
    cout<<"Matrix after transformation: "<<endl;
    for(auto row: matrix1) {
        for(auto i: row)
            cout<< i <<" ";
        cout<<endl;
    }

    vector<vector<int>> matrix2 = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
    setZerosBetter(matrix2);
    cout<<"Matrix after transformation: "<<endl;
    for(auto row: matrix2) {
        for(auto i: row)
            cout<< i <<" ";
        cout<<endl;
    }

    vector<vector<int>> matrix3 = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
    setZerosOptimized(matrix3);
    cout<<"Matrix after transformation: "<<endl;
    for(auto row: matrix3) {
        for(auto i: row)
            cout<< i <<" ";
        cout<<endl;
    } 

    return 0;
}