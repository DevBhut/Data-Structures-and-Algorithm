#include<iostream>
#include<vector>
#include<set>       // -> cannot use unordered_set or unordered_map as it requires hashing and cpp do not have built-in
                    // hashing for complex datatype like vector<int>. Explained in detail at the end.
#include<unordered_set>
#include<algorithm>
using namespace std;


// Brute Force:
vector<vector<int>> three_sum_brute(vector<int> &arr) {
    int n = arr.size();
    set<vector<int>> st;
    for(int i=0; i<n; i++) {
        for(int j=i+1; j<n; j++) {
            for(int k=j+1; k<n; k++) {
                if (arr[i] + arr[j] + arr[k] == 0) {
                    vector<int> temp = {arr[i], arr[j], arr[k]};
                    sort(temp.begin(), temp.end());
                    st.insert(temp);
                }
            }
        }
    }
    if (st.empty())
        return {};
    vector<vector<int>> ans(st.begin(), st.end());
    return ans;
}


// Better Solution:
vector<vector<int>> three_sum_better(vector<int> &arr) {
    int n = arr.size();
    set<vector<int>> st;
    for(int i=0; i<n; i++) {
        unordered_set<int> mp;
        for(int j=i+1; j<n; j++) {
            int req = -(arr[i] + arr[j]);
            if(mp.find(req) != mp.end()) {
                vector<int> temp = {arr[i], arr[j], req};
                sort(temp.begin(), temp.end());
                st.insert(temp);
            }
            mp.insert(arr[j]);
        }
    }
    if (st.empty())
        return {};
    vector<vector<int>> ans(st.begin(), st.end());
    return ans;
}


// Optimal Solution:
vector<vector<int>> three_sum_opti(vector<int> &arr) {
    int n = arr.size();
    sort(arr.begin(), arr.end());
    vector<vector<int>> ans;
    for(int i=0; i<n; i++) {
        if(i!=0 && arr[i] == arr[i-1])
            continue;
        int j = i+1, k = n-1;

        while(j<k) {
            int sum = arr[i] + arr[j] + arr[k];
            if(sum<0)
                j++;
            else if (sum>0)
                k--;
            else {
                vector<int> temp = {arr[i], arr[j], arr[k]};
                ans.push_back(temp);
                j++; 
                k--;
                while(j<k && arr[j] == arr[j-1])
                    j++;
                while(j<k && arr[k] == arr[k+1])
                    k--;
            }
            
        }
    }
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
    vector<int> arr1 = {-1, 0, 1, 2, -1, -4};    // Output: [[-1,-1,2],[-1,0,1]]
    vector<int> arr2 = {0, 2, 3, -4, -6, 7};     // Output: []

    // Call the three_sum functions for arr1
    vector<vector<int>> o1_br = three_sum_brute(arr1);
    vector<vector<int>> o1_be = three_sum_better(arr1);
    vector<vector<int>> o1_op = three_sum_opti(arr1);

    // Call the three_sum functions for arr2
    vector<vector<int>> o2_br = three_sum_brute(arr2);
    vector<vector<int>> o2_be = three_sum_better(arr2);
    vector<vector<int>> o2_op = three_sum_opti(arr2);

    // Print the results for arr1
    cout << "Array1:\n";
    cout << "Brute: ";
    print_result(o1_br);
    cout << "Better: ";
    print_result(o1_be);
    cout << "Opti: ";
    print_result(o1_op);

    // Print the results for arr2
    cout << "\nArray2:\n";
    cout << "Brute: ";
    print_result(o2_br);
    cout << "Better: ";
    print_result(o2_be);
    cout << "Opti: ";
    print_result(o2_op);

    return 69;
}






/*
can i do this : unordered_set<vector<int>> st;
ChatGPT said:
ChatGPT
In C++, you cannot directly use unordered_set<vector<int>> without providing a custom hash function because the standard library does not define a hash function for std::vector<int> by default. 
The reason is that unordered_set relies on hashing to manage its elements, and the hash for complex types like std::vector<int> needs to be explicitly defined.
However, you can use unordered_set<vector<int>> if you provide a custom hash function for std::vector<int>. Here's how you can do it:

Example of how to use unordered_set<vector<int>> with a custom hash function:

cpp
Copy code
#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

// Custom hash function for vector<int>
struct VectorHash {
    size_t operator()(const vector<int>& v) const {
        size_t hash = 0;
        for (int i : v) {
            hash ^= hash * 31 + std::hash<int>()(i);  // Combine hash values for each element
        }
        return hash;
    }
};

int main() {
    // Declare unordered_set with vector<int> and the custom hash function
    unordered_set<vector<int>, VectorHash> st;

    // Example usage
    st.insert({1, 2, 3});
    st.insert({4, 5, 6});

    // Output elements
    for (const auto& vec : st) {
        for (int x : vec) {
            cout << x << " ";
        }
        cout << endl;
    }

    return 0;
}
Explanation:
Custom Hash Function (VectorHash): This function uses a hash combination strategy to generate a unique hash for each vector<int>. It iterates over the vector and combines the hash values of each element.
unordered_set Declaration: The unordered_set takes two template parameters: the type (vector<int>) and the custom hash function (VectorHash).
Key Points:
unordered_set needs a hash function for any user-defined type (like vector<int>).
The custom hash function allows unordered_set to manage vector<int> types by hashing them properly.
This approach allows you to use unordered_set<vector<int>> efficiently.




You said:
can i do that with set? or map?
ChatGPT said:
ChatGPT
Yes, in C++, you can use set<vector<int>> or map<vector<int>, T> without any additional effort, because set and map are ordered containers that do not rely on hashing. 
Instead, they use comparisons to maintain the order of their elements, which is why you don't need a custom hash function.

1. Using set<vector<int>>:
A set in C++ stores its elements in a sorted order using a binary search tree (usually a Red-Black Tree).
The set requires that the type stored in it supports the < (less than) operator for comparisons, and std::vector<int> provides a lexicographical comparison by default.

cpp
Copy code
#include <iostream>
#include <set>
#include <vector>

using namespace std;

int main() {
    // Declare a set of vector<int>
    set<vector<int>> st;

    // Insert some vectors
    st.insert({1, 2, 3});
    st.insert({4, 5, 6});

    // Iterate and print elements
    for (const auto& vec : st) {
        for (int x : vec) {
            cout << x << " ";
        }
        cout << endl;
    }

    return 0;
}
This works because the set uses the < operator on vector<int>, which compares vectors lexicographically (element by element from left to right).


2. Using map<vector<int>, T>:
Similarly, you can use map<vector<int>, T> because std::map also relies on comparisons (using the < operator) to maintain the order of keys.

cpp
Copy code
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    // Declare a map with vector<int> as key and int as value
    map<vector<int>, int> mp;

    // Insert key-value pairs
    mp[vector<int>{1, 2, 3}] = 100;
    mp[vector<int>{4, 5, 6}] = 200;

    // Iterate and print key-value pairs
    for (const auto& [key, value] : mp) {
        for (int x : key) {
            cout << x << " ";
        }
        cout << ": " << value << endl;
    }

    return 0;
}

The map uses the < operator for its key comparisons, which works for vector<int> due to lexicographical ordering.
Why This Works Without Custom Functions:
Lexicographical Comparison: The C++ standard library defines lexicographical comparison for containers like std::vector. 
This means that vectors are compared element by element, in the same way you might compare strings.
In set and map, elements are automatically sorted based on this comparison, so no additional customization is needed.
Summary:
set<vector<int>>: No custom comparator needed; uses lexicographical comparison.
map<vector<int>, T>: No custom comparator needed; keys are compared lexicographically.
For both set and map, the containers automatically sort their elements, unlike unordered_set and unordered_map where you must define a hash function.




You said:
can i convert vector to tuple and then store it in unordered_map, like the following code in python:
temp = [arr[i], arr[j], arr[k]]
temp.sort() 
st.add(tuple(temp))

ChatGPT said:
ChatGPT
Yes, you can convert a vector to a tuple in C++ and store it in an unordered_map or unordered_set. 
However, unlike Python, C++ does not have built-in functionality for converting a vector directly into a tuple. You would have to manually convert the vector to a tuple or use other data structures that fit the situation.
Here's how you can implement a similar approach in C++ to convert a vector to a tuple, and then use it in an unordered_set or unordered_map:

Example with unordered_set<tuple<int, int, int>> in C++:
Convert vector<int> to tuple<int, int, int>:

Since tuples in C++ are fixed-size, you can't directly convert a variable-size vector into a tuple, but you can do it manually for small, fixed-size cases like in your example with three elements.
Also, you need a custom hash function for the tuple because unordered_set requires hashing.
Code Example:

cpp
Copy code
#include <iostream>
#include <unordered_set>
#include <tuple>
#include <vector>
#include <algorithm>

using namespace std;

// Custom hash function for tuple<int, int, int>
struct TupleHash {
    size_t operator()(const tuple<int, int, int>& t) const {
        size_t h1 = hash<int>()(get<0>(t));
        size_t h2 = hash<int>()(get<1>(t));
        size_t h3 = hash<int>()(get<2>(t));
        return h1 ^ (h2 << 1) ^ (h3 << 2); // Combine the hash values
    }
};

int main() {
    // Declare an unordered_set of tuple<int, int, int>
    unordered_set<tuple<int, int, int>, TupleHash> st;

    // Example array with 3 elements
    vector<int> arr = {1, 3, 2};

    // Extract elements and sort them (equivalent to temp.sort() in Python)
    vector<int> temp = {arr[0], arr[1], arr[2]};
    sort(temp.begin(), temp.end());

    // Convert sorted vector to a tuple
    tuple<int, int, int> tpl = make_tuple(temp[0], temp[1], temp[2]);

    // Insert the tuple into the unordered_set
    st.insert(tpl);

    // Check if the tuple exists in the set
    if (st.find(tpl) != st.end()) {
        cout << "Tuple found in the set!" << endl;
    }

    return 0;
}
Key Points:
Manual Conversion: We manually converted a 3-element vector<int> into a tuple<int, int, int> using make_tuple.
Custom Hash Function: Since unordered_set and unordered_map rely on hash values, a custom hash function for the tuple is provided (TupleHash).
Sorting: Like the Python example where you sort the list before converting it to a tuple, the vector is sorted using sort(temp.begin(), temp.end()).
Summary:
You can achieve the same effect as the Python code in C++, but you must manually handle the conversion from vector to tuple and provide a custom hash function when using unordered_set or unordered_map.
For small, fixed-size vectors (like the 3-element case), converting to tuple is feasible and works well. However, for larger, dynamically sized vectors, it’s better to stick with a vector and define a custom hash function for the unordered_set or unordered_map.

*/