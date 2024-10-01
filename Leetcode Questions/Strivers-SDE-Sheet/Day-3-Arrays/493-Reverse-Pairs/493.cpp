#include<iostream>
#include<vector>
using namespace std;

// Brute Force Solution
int reverse_pairs_brute(vector<int> arr) {
    int n = arr.size();
    int count = 0;
    for(int i=0; i<n; i++) {
        for(int j = i+1; j<n; j++) {
            if(arr[i] > 2*arr[j])
                count++;
        }
    }
    return count;
}



// Optimal Solution

int count_pairs(vector<int> &arr, int low, int mid, int high) {
    int count = 0;
    int right = mid + 1;
    for(int i=low; i<mid+1; i++) {
        while(right <= high && arr[i] > 2*arr[right])
            right++;
        count += (right - (mid + 1)); 
    }
    return count;
}

void merge(vector<int> &arr, int low, int mid, int high) {
    vector<int> temp;
    int left = low;
    int right = mid + 1;

    while(left <= mid && right <= high) {
        if(arr[left] <= arr[right]) {
            temp.push_back(arr[left]);
            left++;
        }
        else {
            temp.push_back(arr[right]);
            right++;
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

}

int merge_sort(vector<int> &arr, int low, int high) {
    int count = 0;
    if (low >= high)
        return count;
    
    int mid = (low + high)/2;
    count += merge_sort(arr, low,  mid);
    count += merge_sort(arr, mid+1, high);
    count += count_pairs(arr, low, mid, high);
    merge(arr, low, mid, high);
    return count;
}

int reverse_pairs_opti(vector<int> &arr) {
    int n = arr.size();
    return merge_sort(arr, 0, n-1);
}


int main() {
    vector<int> arr1 = {1, 3, 2, 3, 1};     // output = 2
    vector<int> arr2 = {2, 4, 3, 5, 1};     // output = 3
    int output1_b = reverse_pairs_brute(arr1);
    int output2_b = reverse_pairs_brute(arr2);

    int output1_o = reverse_pairs_opti(arr1);
    int output2_o = reverse_pairs_opti(arr2);

    cout<<"Brute Force Method: Output1: "<<output1_b<<". Output2: "<<output2_b<<".";
    cout<<endl;
    cout<<"Optimal Method: Output1: "<<output1_o<<". Output2: "<<output2_o<<".";

    return 0;
}