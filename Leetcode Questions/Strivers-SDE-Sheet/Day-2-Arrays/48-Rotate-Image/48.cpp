// Only writing optimized code here. Rest is in python

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void rotateImage(vector<vector<int>> &arr) {
    int n = arr.size();
    // Transposing Matrix
    for(int i=0; i<n; i++) {
        for(int j=0; j<i; j++) {
            int temp = arr[i][j];
            arr[i][j] = arr[j][i];
            arr[j][i] = temp;
        }
    }
    // Reversing each row
    for(int i=0; i<n; i++)
        reverse(arr[i].begin(), arr[i].end());
}


int main() {
    vector<vector<int>> matrix = {{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}};
    cout<<"Matrix before rotating: "<<endl;
    for(auto row: matrix) {
        for(int i=0; i<matrix.size(); i++)
            cout<<row[i]<<"\t";
        cout<<endl;
    }
    cout<<endl;
    cout<<"Matrix after rotating: "<<endl;
    rotateImage(matrix);
    for(auto row: matrix) {
        for(int i=0; i<matrix.size(); i++)
            cout<<row[i]<<"\t";
        cout<<endl;
    }
}