// Only implementing the optimized solution here. Rest all is in python

#include<iostream>
#include<vector>
using namespace std;

int maxSubArr(vector<int> &arr) {
    int n = arr.size();
    int sum = 0, maxi = INT16_MIN;
    for(int i=0; i<n; i++) {
        sum += arr[i];
        maxi = max(maxi, sum);
        if(sum < 0)
            sum = 0;
    }
    if(maxi < 0)
        maxi = 0;
    return maxi;
}


int main() {
    vector<int> arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout<<"Maximum Sum of Subarray: "<<maxSubArr(arr);
    return 0;
}