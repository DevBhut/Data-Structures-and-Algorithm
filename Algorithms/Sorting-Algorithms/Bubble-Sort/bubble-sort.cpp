#include<iostream>
#include<vector>
using namespace std;

void swap1(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}


void bubble_sort_vec(vector<int> &arr) {
    int n = arr.size();
    for(int i=1; i<n; i++) {
        for(int j=0; j<n-i; j++) {
            if(arr[j] > arr[j+1])
                swap1(arr[j], arr[j+1]);
        }
    }
}


void bubble_sort_opti(vector<int> &arr) {
    int n = arr.size();
    bool swap = false;
    for(int i=1; i<n; i++) {
        for(int j=0; j<n-i; j++) {
            if(arr[j] > arr[j+1]) {
                swap1(arr[j], arr[j+1]);
                swap = true;
            }
        }
        if(!swap)
            break;
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
    vector<int> arr = form_vec();
    bubble_sort_opti(arr);
    cout<<"Sorted Array: "<<endl;
    for(int i: arr)
        cout<< i <<" ";
    cout<<endl;
    return 0;

}
