#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;


// Brute Force Solution
int length_0_sum_brute(vector<int> &arr) {
    int n = arr.size();
    int longest = 0;
    for(int i=0; i<n; i++) {
        int sum = 0;
        for(int j=i; j<n; j++) {
            sum += arr[j];
            if(sum == 0) {
                int len = j-i+1;
                longest = max(longest, len);
            }
        }
    }
    return longest;
}


// Optimal Soltuion
int length_0_sum_opti(vector<int> &arr) {
    int n = arr.size();
    int sum = 0, longest = 0;
    unordered_map<int, int> mp;
    for(int i=0; i<n; i++) {
        sum += arr[i];
        if(sum == 0)
            longest = i+1;
        else if(mp.find(sum) != mp.end())
            longest = max(longest, i-mp[sum]);
        else
            mp[sum] = i;
    }
    return longest;
}



int main() {
    vector<int> arr1 = {15, -2, 2, -8, 1, 7, 10, 23};   // output: 5
    vector<int> arr2 = {2, 10, 4};                      // output: 0
    vector<int> arr3 = {1, 3, 0, -5};                   // output: 1

    int o1_br = length_0_sum_brute(arr1);
    int o2_br = length_0_sum_brute(arr2);
    int o3_br = length_0_sum_brute(arr3);

    int o1_op = length_0_sum_opti(arr1);
    int o2_op = length_0_sum_opti(arr2);
    int o3_op = length_0_sum_opti(arr3);    

    cout<<"Array1: Brute: "<<o1_br<<". Opti: "<<o1_op<<". \n";
    cout<<"Array2: Brute: "<<o2_br<<". Opti: "<<o2_op<<". \n";
    cout<<"Array3: Brute: "<<o3_br<<". Opti: "<<o3_op<<". \n";

    return 69;
}