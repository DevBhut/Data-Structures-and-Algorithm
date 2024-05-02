#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


bool searchMatrixOpti(vector<vector<int>> &matrix, int target) {
    int n = matrix.size(), m = matrix[0].size();
    int l=0, h=n*m;
    while(l<h) {
        int mid = (l+h)/2;
        int row = mid / m;
        int col = mid % m;
        if(target == matrix[row][col])
            return true;
        else if(target > matrix[row][col])
            l = mid+1;
        else
            h = mid;
    }
    return false;
}



int main() {
    vector<vector<int>> matrix = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    int target1 = 3, target2 = 13;
    cout<<"Is target in matrix: "<<searchMatrixOpti(matrix, target1);
    return 0;
}