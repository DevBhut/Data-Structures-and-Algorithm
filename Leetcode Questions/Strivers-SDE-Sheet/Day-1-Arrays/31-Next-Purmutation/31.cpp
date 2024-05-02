/* 
This is the optimal solution of this problem. Time Complexity -> O(n).  In-detai: O(3n)

The Brute Force Solution of this problem is first finding all the possible permuatations of all the digits
given in the array, store all of them in sorted order, and then search for the current one, 
and return the next one. 
Time Complexity -> O(n! * n).  In-detail: finding all permuataions take n!*n and searching it takes n!(worst case)

There is also a better solution, but only in cpp. As cpp contains next_permutation() -> in-built func under algorithm header
Implemented below.

*/
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void nextPer(vector<int>& arr) {
    int n = arr.size(), ind = -1;

    for(int i = n-2; i>=0; i--) {
        if(arr[i+1] > arr[i]) {
            ind = i;
            break;
        }
    }

    if(ind == -1) 
        reverse(arr.begin(), arr.end());
    else {
        for(int i = n-1; i>ind; i--) {
            if(arr[i] > arr[ind]) {
                swap(arr[i], arr[ind]);
                break;
            }
        }
        reverse(arr.begin() + ind + 1, arr.end());
    }
}


int main() {
    vector<int> arr = {2, 1, 5, 4, 3, 0, 0};
    nextPer(arr);
    cout<<"Next Permuatation is: "<<endl;
    for(int i: arr)
        cout<<i<<" ";
    cout<<endl;
    next_permutation(arr.begin(), arr.end());
    cout<<"Next Permutation of the above is (using in-built function): "<<endl;
    for(int i: arr)
        cout<<i<<" ";
    return 0;

}