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


int partition(vector<int> &arr, int low, int high) {
    int pivot = arr[low];
    int i = low;
    int j = high;
    while(i<j) {
        while(arr[i]<=pivot && i<high)
            i++;
        while(arr[j]>pivot && j>low)
            j--;
        if(i<j)
            swap1(arr[i], arr[j]);
    }
    swap1(arr[low], arr[j]);
    return j;
}


void quick_sort(vector<int> &arr, int low, int high) {
    if(low < high) {
        int pivot = partition(arr, low, high);
        quick_sort(arr, low, pivot-1);
        quick_sort(arr, pivot+1, high);
    }
}


void quick_sort_decode(vector<int> &arr, int low, int high) {
    if(low < high) {
        cout<<"Array before pivoting: \n";
        for(int i: arr)
            cout<<i<<"    ";

        int pivot = partition(arr, low, high);

        cout<<"\nArray after placing pivot(1st) element in correct position: \n";
        for(int i: arr)
            cout<<i<<"    ";
        cout<<"Correct / Pivot position: "<<pivot<<"\n\n";

        quick_sort_decode(arr, low, pivot-1);
        quick_sort_decode(arr, pivot+1, high);
    }
}



int main() {
    vector<int> arr = form_vec();
    int n = arr.size();
    quick_sort(arr, 0, n-1);
    cout<<"Sorted Array: "<<endl;
    for(int i: arr)
        cout<< i <<" ";
    cout<<endl;
    return 0;

}