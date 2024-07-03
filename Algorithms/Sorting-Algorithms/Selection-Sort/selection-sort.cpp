#include<iostream>
#include<vector>
using namespace std;

void swap1(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}


void selection_sort_arr(int arr[], int n) {
    for(int i=0; i<n-1; i++) {
        int mini = i;
        for(int j=i; j<n; j++) {
            if(arr[j] < arr[mini])
                mini = j;
        }
        swap1(arr[i], arr[mini]);
    }
}


void selection_sort_vec(vector<int> &arr) {
    int n = arr.size();
    for(int i=0; i<n-1; i++) {
        int mini = i;
        for(int j=i; j<n; j++) {
            if(arr[j] < arr[mini])
                mini = j;
        }
        swap1(arr[i], arr[mini]);
    }
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


int main() {
    // For integer array
    // int n;
    // cout<<"Enter the number of elements of the array: ";
    // cin >> n;
    // int arr[n];
    // cout<<"Enter the elements of the array: "<<endl;
    // for(int i=0; i<n; i++) 
    //     cin >> arr[i];
    // cout<<endl;
    // cout<<"The array is: "<<endl;
    // for(int i: arr)
    //     cout<< i <<" ";
    // cout<<endl<<endl;
    // selection_sort_arr(arr, n);
    vector<int> arr = form_vec();
    selection_sort_vec(arr);
    cout<<"Sorted Array: "<<endl;
    for(int i: arr)
        cout<< i <<" ";
    cout<<endl;
    return 0;

}
