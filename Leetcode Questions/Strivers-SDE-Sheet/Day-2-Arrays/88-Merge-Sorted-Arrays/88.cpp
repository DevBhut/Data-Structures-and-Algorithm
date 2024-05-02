// Only Optimal Solution here, rest in python

#include<iostream>
#include<vector>
using namespace std;

void mergeSortedOpti(vector<int>& nums1, int n, vector<int>& nums2, int m) {
    int i = n - 1;
    int j = m - 1;
    int k = n + m - 1;  
    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
}


int main()
{
    vector<int> nums1 = {1,2,3,0,0,0};
    vector<int> nums2 = {2,5,6};
    mergeSortedOpti(nums1, 3, nums2, 3);
    cout<<"After calling the function: "<<endl;
    for(auto i: nums1)
        cout<<i<<" ";
    return 0;
}

