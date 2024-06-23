#include<iostream>
#include<vector>
using namespace std;


// DP Solution
int countPathsBetter(int i, int j, int m, int n, vector<vector<int>> &dp) {
    if( i == (m-1) && j == (n-1) )
        return 1;
    if( i>=m || j>=n )
        return 0;
    if( dp[i][j]!=-1)
        return dp[i][j];
    else
        return dp[i][j] = countPathsBetter(i+1, j, m, n, dp) + countPathsBetter(i, j+1, m, n, dp);
}
int uniquePathsBetter(int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n, -1));
    int num = countPathsBetter(0, 0, m, n, dp);
    if( m==1 && n==1)
        return num;
    return dp[0][0];    
}


// Opti Sol
int nCr(int n, int r) {
    // cout<<"Inside nCr Function. n: "<<n<<" r: "<<r<<endl;  --> debugging 
    double ans = 1;
    for(int i=0; i<r; i++) {
        ans = ans*(n-i)/(i+1);
        // cout<<"Inside for loop. Itr "<<i<<". ans: "<<ans<<endl; --> debugging
        // ans = ans/(i+1);
    }
    // cout<<"Inside nCr Function. ans: "<<ans<<endl;  --> debugging
    return (int)ans;
}
int uniquePathsOpti(int m, int n) {
    return nCr(m+n-2, n-1);
}



int main() {
    int m = 3, n = 5;
    int totalCounts = uniquePathsOpti(m, n);
    cout<<"The total number of unique paths for "<<m<<"x"<<n<<" matrix is: "<<totalCounts<<endl;
    return 0;
}

