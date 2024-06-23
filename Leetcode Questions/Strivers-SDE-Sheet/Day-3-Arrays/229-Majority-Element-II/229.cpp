#include<iostream>
#include<vector>
#include<map>
using namespace std;

vector<int> majorityBetter(vector<int> &arr) {
    int n = arr.size();
    vector<int> ele;
    map<int, int> mpp;
    for(int i=0; i<n; i++) {
        mpp[arr[i]]++;
        if(mpp[arr[i]] > n/3)
            ele.push_back(arr[i]);
        if(ele.size() == 2)
            break;
    }
    return ele;
}


vector<int> majorityOpti(vector<int> &arr) {
    int n = arr.size();
    int ele1 = INT16_MIN, ele2 = INT16_MIN;
    int cnt1 = 0, cnt2 = 0;
    
    for(int i=0; i<n; i++) {
        if(cnt1 == 0 && ele2 != arr[i]) {
            cnt1++;     ele1 = arr[i]; 
        }
        else if(cnt2 == 0 && ele1 != arr[i]) {
            cnt2++;     ele2 = arr[i];
        }
        else if(arr[i] == ele1)
            cnt1++;
        else if(arr[i] == ele2)
            cnt2++;
        else
            cnt1--, cnt2--; 
    }

    vector<int> ele;
    cnt1 = 0, cnt2 = 0;
    for(int i=0; i<n; i++) {
        if(arr[i] == ele1)      cnt1++;
        if(arr[i] == ele2)      cnt2++;
    }
    if(cnt1 > n/3)      ele.push_back(ele1);
    if(cnt2 > n/3)      ele.push_back(ele2);
    return ele;
}


int main() {
    vector<int> arr = {1, 2, 3, 1, 3, 2, 1, 2};
    vector<int> out = majorityOpti(arr);
    for(int i: out)
        cout<<i<<" ";
    return 0;
}