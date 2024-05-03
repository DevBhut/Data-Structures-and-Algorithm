#include<iostream>
#include<vector>
#include<map>
using namespace std;


// Using Hash Map
int majorityBetter(vector<int> &&arr) {
    int n = arr.size();
    map<int, int> cnt;
    for(int i=0; i<n; i++) 
        cnt[arr[i]]++;
    for(auto i: cnt)
        if (i.second > n/2)
            return i.first;
    return -1;
}


int majorityOpti(vector<int> &arr) {
    int n = arr.size();
    int count = 0;
    int ele = NULL;
    for(int i=0; i<n; i++) {
        if(count == 0) {
            count = 1;
            ele = arr[i];
        }
        else if(ele == arr[i])
            count++;
        else
            count--;
    }
    return ele;
}