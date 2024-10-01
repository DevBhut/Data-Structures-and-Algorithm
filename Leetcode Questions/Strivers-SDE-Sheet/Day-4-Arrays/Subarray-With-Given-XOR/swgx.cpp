#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;


// Optimal Solution
int count_subarrays_opti(vector<int> &arr, int k) {
    int n = arr.size();
    unordered_map<int, int> mp;
    int count = 0; 
    int Xor = 0;
    mp[Xor] = 1;

    for(int i=0; i<n; i++) {
        Xor ^= arr[i];
        int y = Xor ^ k;
        if(mp.find(y) != mp.end())
            count += mp[y];
        mp[Xor] += 1;
    } 

    return count;
}



int main() {
    vector<int> arr1 = {4, 2, 2, 6, 4};
    int k1 = 6;
    
    vector<int> arr2 = {5, 6, 7, 8, 9};
    int k2 = 5;
    
    vector<int> arr3 = {4, 2, 6, 6};
    int k3 = 6;
    
    // Optimized outputs
    int o1_op = count_subarrays_opti(arr1, k1);
    int o2_op = count_subarrays_opti(arr2, k2);
    int o3_op = count_subarrays_opti(arr3, k3);
    
    // Print the results
    cout << "Opti: Output1: " << o1_op << ", Output2: " << o2_op << ", Output3: " << o3_op << endl;
    
    return 69;
}