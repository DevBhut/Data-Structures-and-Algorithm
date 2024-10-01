#include<iostream>
#include<vector>
#include<unordered_map>
#include<unordered_set>
#include<string>
#include<typeinfo>      // to find the data-type of the variable
using namespace std;


// Better solution
int substring_better(string arr) {
    int n = arr.size();     // can also use arr.length(), arr.size() is general and works with vector, arr, queues etc. arr.length() is specific to strings
    if(n == 0)
        return 0;
    int l = 0;
    int longest = 0;
    unordered_set<char> st;
    for(int r=0; r<n; r++) {
        if(st.find(arr[r]) != st.end()) {
            while( l<r && (st.find(arr[r]) != st.end()) ) {
                st.erase(arr[l]);
                l++;
            }
        }
        st.insert(arr[r]);
        longest = max(longest, r-l+1);
    }
    return longest;
}



// Optimal Solution
int substring_opti(string arr) {
    int n = arr.size();
    int l = 0, r = 0, longest = 0;
    unordered_map<char, int> mp;
    while(r < n) {
        if(mp.find(arr[r]) != mp.end())
            l = max(l, mp[arr[r]] + 1);
        mp[arr[r]] = r;
        longest = max(longest, r-l+1);
        r++;
    }
    return longest;
}



int main() {
    string arr1 = "abcabcbb";   // output: 3
    string arr2 = "bbbb";       // output: 1
    string arr3 = "pwwkew";     // output: 3

    cout<<"Type of arr1[1]: "<<typeid(arr1[1]).name()<<endl;;

    int o1_be = substring_better(arr1);
    int o2_be = substring_better(arr2);
    int o3_be = substring_better(arr3);
        
    int o1_op = substring_opti(arr1);
    int o2_op = substring_opti(arr2);
    int o3_op = substring_opti(arr3);

    cout << "Better: \nOp1: " << o1_be << ", Op2: " << o2_be << ", Op3: " << o3_be << "\n";
    cout << "Opti: \nOp1: " << o1_op << ", Op2: " << o2_op << ", Op3: " << o3_op << "\n";

    return 69;

}