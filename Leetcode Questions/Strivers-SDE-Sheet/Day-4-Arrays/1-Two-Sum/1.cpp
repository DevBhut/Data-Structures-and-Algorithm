#include<iostream>
#include<vector>
#include<unordered_map>
#include<algorithm>
using namespace std;

// Opitmal solution: hashmap. TC: O(n), SC: O(n)
vector<int> two_sum(vector<int> &arr, int target) {
    int n = arr.size();
    unordered_map<int, int> mp;
    for(int i=0; i<n; i++) {
        int req = target - arr[i];
        if(mp.find(req) != mp.end())
            return {mp[req], i};
        mp[arr[i]] = i;
    }
    return {};
}


// Variant 2: return True if pair exists, else False. TC: O(n) + O(n*log(n)), SC: O(1)
bool two_sum_var2(vector<int> &arr, int target) {
    int n = arr.size();
    sort(arr.begin(), arr.end());
    int left = 0, right = n-1;
    while(left <= right) {
        if(arr[left] + arr[right] == target)
            return true;
        
        if(arr[left] + arr[right] < target)
            left++;
        else
            right--;
    }
    return false;
}


int main() {
    vector<int> arr = {2, 6, 5, 8, 11};
    vector<int> op = two_sum(arr, 14);      // Output: {1, 3}
    cout<<"Output: {"<<op[0]<<", "<<op[1]<<"}"<<endl;
    cout<<"Do 14 as a sum of pairs exist in arr? -> "<<two_sum_var2(arr, 14)<<endl;
    cout<<"Do 15 as a sum of pairs exist in arr? -> "<<two_sum_var2(arr, 15);
    return 69;
}
