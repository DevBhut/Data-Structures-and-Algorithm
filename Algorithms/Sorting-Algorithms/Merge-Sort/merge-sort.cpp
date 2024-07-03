#include<iostream>
#include<vector>
using namespace std;

void swap1(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}


vector<int> form_vec() {
    int n;
    cout<<"Enter the number of elements of the array: ";
    cin >> n;
    vector<int> arr(n);
    cout<<"Enter the elements of the array: "<<endl;
    for(int i=0; i<n; i++)
        cin >> arr[i];
    cout<<endl;
    cout<<"The array is: "<<endl;
    for(int i: arr)
        cout<< i <<" ";
    cout<<endl<<endl;
    return arr;
}


void merge(vector<int> &arr, int low, int mid, int high) {
    vector<int> temp;
    int left = low;
    int right = mid+1;
    while(left <= mid && right <= high) {
        if (arr[left] <= arr[right]) {
            temp.push_back(arr[left]);
            left++;
        }
        else {
            temp.push_back(arr[right]);
            right++;
        }
    }
    while(left<=mid) {
        temp.push_back(arr[left]);
        left++;
    }
    while(right<=high) {
        temp.push_back(arr[right]);
        right++;
    }
    for(int i=low; i<=high; i++)
        arr[i] = temp[i-low];
}


void merge_sort(vector<int> &arr, int low, int high) {
    if(low>=high)
        return;
    int mid = (low+high)/2;
    merge_sort(arr, low, mid);
    merge_sort(arr, mid+1, high);
    merge(arr, low, mid, high);
}


int main() {
    vector<int> arr = form_vec();
    int n = arr.size();
    merge_sort(arr, 0, n-1);
    cout<<"Sorted Array: "<<endl;
    for(int i: arr)
        cout<< i <<" ";
    cout<<endl;
    return 0;

}
