#include<iostream>
#include<vector>
using namespace std;

// Brute Force Solution
int count_inversions_brute(vector<int> arr) {
    int n = arr.size();
    int count = 0;
    for(int i=0; i<n; i++) {
        for(int j = i+1; j<n; j++) {
            if(arr[i] > arr[j])
                count ++;
        }
    }
    return count;
}


// Optimal Solution
int merge(vector<int> &arr, int low, int mid, int high) {
    vector<int> temp;
    int left = low;
    int right = mid + 1;
    int count = 0;

    while(left <= mid && right <= high) {
        if (arr[left] <= arr[right]) {  
            temp.push_back(arr[left]);
            left++;
        }
        else {
            temp.push_back(arr[right]);
            right++;
            count += (mid - left + 1);
        }
    }

    while(left <= mid) {
        temp.push_back(arr[left]);
        left++;
    }

    while(right <= high) {
        temp.push_back(arr[right]);
        right++;
    }

    for(int i=low; i<=high; i++) {
        arr[i] = temp[i-low];
    }
    
    return count;
}


int merge_sort(vector<int> &arr, int low, int high) {
    int count = 0;
    if(low >= high) {
        return count;
    }
    int mid = (low + high)/2;
    count += merge_sort(arr, low, mid);
    count += merge_sort(arr, mid+1, high);
    count += merge(arr, low, mid, high);
    return count;
}


int count_inversions_opti(vector<int> &arr) {
    int n = arr.size();
    return merge_sort(arr, 0, n-1);
}


int main() {
    vector<int> arr1 = {3, 2, 1};    // Output: 3
    vector<int> arr2 = {5, 3, 2, 1, 4};     // Output: 7
    int output1 = count_inversions_opti(arr1);
    int output2 = count_inversions_opti(arr2);
    cout<<"Output1: "<<output1<<". Output2: "<<output2;
    return 0;
}