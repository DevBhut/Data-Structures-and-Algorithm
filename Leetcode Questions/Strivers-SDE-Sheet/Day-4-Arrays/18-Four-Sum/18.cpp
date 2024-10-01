#include<iostream>
#include<vector>
#include<set>
#include<unordered_set>
#include<algorithm>
using namespace std;

// Better Solution:
vector<vector<int>> four_sum_better(vector<int> &arr, int target) {
    int n = arr.size();
    set<vector<int>> st;
    for(int i=0; i<n; i++) {
        for(int j=i+1; j<n; j++) {
            unordered_set<int> mp;
            for(int k=j+1; k<n; k++) {
                long long sum = arr[i] + arr[j];
                sum += arr[k];
                long long req = target - sum;
                if(mp.find(req) != mp.end()) {
                    vector<int> temp = {arr[i], arr[j], arr[k], int(req)};
                    sort(temp.begin(), temp.end());
                    st.insert(temp);
                }
                mp.insert(arr[k]);
            }
        }
    }

    if(st.empty())
        return {{}};
    vector<vector<int>> ans(st.begin(), st.end());
    return ans;
}


// Optimal Solution:
vector<vector<int>> four_sum_opti(vector<int> &arr, int target) {
    int n = arr.size();
    sort(arr.begin(), arr.end());
    vector<vector<int>> ans;

    for(int i=0; i<n; i++) {
        if(i!=0 && arr[i]==arr[i-1])
            continue;
        
        for(int j=i+1; j<n; j++) {
            if(j!=i+1 && arr[j]==arr[j-1])
                continue;
            
            // 2 variable/moving pointers
            int k=j+1;
            int l=n-1;

            while(k<l) {
                long long sum = arr[i] + arr[j];
                sum += arr[k]; 
                sum += arr[l];

                if(sum == target) {
                    ans.push_back({arr[i], arr[j], arr[k], arr[l]});
                    k++;
                    l--;

                    while(k<l && arr[k] == arr[k-1])
                        k++;
                    while(k<l && arr[l] == arr[l+1])
                        l--;
                }

                else if(sum < target)
                    k++;
                else
                    l--;
            }
        }
    }

    if (ans.empty())
        return {{}};
    return ans;
}


// Utility function to print 2D vector
void print_result(const vector<vector<int>>& result) {
    cout << "[";
    for (const auto& triplet : result) {
        cout << "[";
        for (int num : triplet) {
            cout << num << " ";
        }
        cout << "] ";
    }
    cout << "]\n";
}

int main() {
    // Define the input arrays
    vector<int> arr1 = {4, 3, 3, 4, 4, 2, 1, 2, 1, 1};    // Output: [[1 1 3 4 ] [1 2 2 4 ] [1 2 3 3 ]]
    int target1 = 9;
    vector<int> arr2 = {0, 2, 3, -4, -6, 7};     // Output: [[]]
    int target2 = 40;

    // Call the three_sum functions for arr1
    vector<vector<int>> o1_be = four_sum_better(arr1, target1);
    vector<vector<int>> o1_op = four_sum_opti(arr1, target1);

    // Call the four_sum functions for arr2
    vector<vector<int>> o2_be = four_sum_better(arr2, target2);
    vector<vector<int>> o2_op = four_sum_opti(arr2, target2);

    // Print the results for arr1
    cout << "Array1:\n";
    cout << "Better: ";
    print_result(o1_be);
    cout << "Opti: ";
    print_result(o1_op);

    // Print the results for arr2
    cout << "\nArray2:\n";
    cout << "Better: ";
    print_result(o2_be);
    cout << "Opti: ";
    print_result(o2_op);

    return 69;
}


