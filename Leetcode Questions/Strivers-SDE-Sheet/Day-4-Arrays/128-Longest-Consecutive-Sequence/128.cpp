#include<iostream>
#include<vector>
#include<unordered_set>
#include<algorithm>
using namespace std;

// Better Solution
int longest_consecutive_better(vector<int> &arr) {
    int n = arr.size();
    if(n == 0)
        return 0;
    sort(arr.begin(), arr.end());
    int longest = 1;
    int curr = 1;
    int prev = arr[0];
    for(int i=1; i<n; i++) {
        if(prev == arr[i] - 1) {
            prev = arr[i];
            curr++;
        }
        else if(prev != arr[i]) {
            prev = arr[i];
            curr = 1;
        }
        longest = max(longest, curr);
    }
    return longest;
}


// Optimal Solution
int longest_consecutive_opti(vector<int> &arr) {
    int n = arr.size();
    if(n == 0)
        return 0;

    int longest = 1;    
    unordered_set<int> mp(arr.begin(), arr.end());
    
    // for(int i=0; i<n; i++) 
    //     mp.insert(arr[i]);

    
    for(int ele: mp) {
        if(mp.find(ele - 1) == mp.end()) {
            int curr = 1;
            int x = ele;
            while(mp.find(x+1) != mp.end()) {
                x += 1;
                curr += 1;
            }
            longest = max(longest, curr);
        }
    }
    return longest;
}



int main() {
    vector<int> arr1 = {100, 4, 200, 1, 3, 2};       // output: 4
    vector<int> arr2 = {0, 3, 7, 2, 5, 8, 4, -1, 6, 0, 1};   // output: 10

    int o1_be = longest_consecutive_better(arr1);
    int o1_op = longest_consecutive_opti(arr1);
    
    int o2_be = longest_consecutive_better(arr2);
    int o2_op = longest_consecutive_opti(arr2);

    cout<<"Array1: Better: "<<o1_be<<". Opti: "<<o1_op<<". \n";
    cout<<"Array2: Better: "<<o2_be<<". Opti: "<<o2_op<<". \n";

    return 69;
}   