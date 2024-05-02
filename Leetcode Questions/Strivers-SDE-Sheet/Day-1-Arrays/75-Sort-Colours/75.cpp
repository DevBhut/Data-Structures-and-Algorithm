#include<iostream>
#include<vector>
using namespace std;


void sortColors(vector<int>& arr ) {
        int right = arr.size() - 1;
        int i = 0, left = 0;
        while(i <= right){
            if(arr[i] == 0){
                swap(arr[i], arr[left]);
                left++;    i++;
            }
            else if(arr[i] == 2){
                swap(arr[i], arr[right]);
                right--;
            }
            else{
                i++;
            }
        }
    }


int main() {
    vector<int> colors = {0, 1, 2, 1, 2, 0, 2, 0, 1, 2, 0};
    cout<<"Array: "<<endl;
    for(int i: colors)
        cout<<i<<" ";
    cout<<endl<<endl;
    sortColors(colors);
    cout<<"After Sorting: "<<endl;
    for(int i: colors)
        cout<<i<<" ";
    return 0;
}