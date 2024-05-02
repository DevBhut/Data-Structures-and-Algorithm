#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
using namespace std;

bool checkRotation(vector<vector<int>> &mat, vector<vector<int>> &target) {
    bool check[4];
	memset(check,true,sizeof(check));
    int n = mat.size();
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(mat[i][j] != target[i][j])       check[0] = false;
            if(mat[i][j] != target[n-j-1][i])    check[1] = false;
            if(mat[i][j] != target[n-i-1][n-j-1])    check[2] = false;
            if(mat[i][j] != target[j][n-i-1])    check[3] = false;
        }
    }
    return check[0] || check[1] || check[2] || check[3];
}


bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        int m = mat.size(), k = 3;
        if (mat == target)
            return true;
        while (k-- != 0) {
            for (int i = 0; i < m; i++) {
                for (int j = 0; j <= i; j++) {
                    swap(mat[i][j], mat[j][i]);
                }
            }
            for (int i = 0; i < m; i++) {
                reverse(mat[i].begin(), mat[i].end());
            }
            if (mat == target) return true;
        }
        return false;
    }