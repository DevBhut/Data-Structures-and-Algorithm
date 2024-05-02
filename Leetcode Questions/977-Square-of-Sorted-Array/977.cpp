#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


vector<int> sortedSquares(vector<int> &arr) {
    int n = arr.size(), sep = -1;
    vector<int> final;

    for(int i=0; i<n; i++) {
        if(arr[i] >= 0) {
            sep = i;
            break;
        }
    }

    if(sep == -1) {
        reverse(arr.begin(), arr.end());
        for(int i: arr)
            final.push_back(i*i);
        return final;
    }

    int left = sep - 1, right = sep;
    while(left >= 0 && right < n) {
        if(arr[right] < abs(arr[left])) {
            final.push_back(arr[right]*arr[right]);
            right++;
        }
        else {
            final.push_back(arr[left]*arr[left]);
            left--;
        }
    }

    while(left >= 0) {
        final.push_back(arr[left]*arr[left]);
        left--;
    }

    while(right < n) {
        final.push_back(arr[right]*arr[right]);
        right++;
    }

    return final;
}




int main() {
    vector<int> nums = {-4,-1,0,3,10};
    vector<int> nums1 = {-7,-3,2,3,11};
    // vector<int> ans = sortedSquares(nums);
    cout<<"Sorted Squares: "<<endl;
    for(int i: sortedSquares(nums)) {
        cout<<i<<" ";
    }
    return 0;
}