#include<iostream>
#include<vector>
using namespace std;

int findDuplicateOpti(vector<int> &arr) {
    int slow = arr[0], fast = arr[0];
    while(true) {
        slow = arr[slow];
        fast = arr[arr[fast]];
        if(slow == fast)
            break;
    }
    fast = arr[0];
    while(slow != fast) {
        slow = arr[slow];
        fast = arr[fast];
    }
    return slow;
}


int main() {
    vector<int> nums = {1, 3, 4, 2, 2};
    cout<<findDuplicateOpti(nums);
    return 0;
}

