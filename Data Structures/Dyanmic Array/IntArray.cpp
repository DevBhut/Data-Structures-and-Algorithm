#include <iostream>
#include <algorithm>
using namespace std;

class IntArray {
private:
    static const int Default_Cap = 1 << 3;

public:
    int* arr;
    int len;
    int capacity;

    // Initialize the array with a default capacity
    IntArray() : len(0), capacity(Default_Cap) {
        arr = new int[capacity];
    }

    // Initialize the array with a certain capacity
    IntArray(int capacity) : len(0), capacity(max(capacity, 0)) {
        arr = new int[capacity];
    }

    // Given an array make it a dynamic array!
    IntArray(int* array, int size) : len(size), capacity(size) {
        if (array == nullptr) throw std::invalid_argument("Array cannot be null");
        arr = new int[capacity];
        std::copy(array, array + size, arr);
    }

    // Destructor to free memory
    ~IntArray() {
        delete[] arr;
    }

    // Returns the size of the array
    int size() {
        return len;
    }

    // Returns true/false on whether the array is empty
    bool isEmpty() {
        return len == 0;
    }

    // To get/set values without method call overhead you can do
    // array_obj.arr[index] instead, you can gain about 10x the speed!
    int get(int index) {
        return arr[index];
    }

    void set(int index, int elem) {
        arr[index] = elem;
    }

    // Add an element to this dynamic array
    void add(int elem) {
        if (len >= capacity) {
            if (capacity == 0) capacity = 1;
            else capacity *= 2;  // double the size
            int* newArr = new int[capacity];
            std::copy(arr, arr + len, newArr);
            delete[] arr;
            arr = newArr;
        }
        arr[len++] = elem;
    }

    // Removes the element at the specified index in this list.
    // If possible, avoid calling this method as it take O(n) time
    // to remove an element (since you have to reconstruct the array)
    void removeAt(int rm_index) {
        std::copy(arr + rm_index + 1, arr + len, arr + rm_index);
        --len;
        --capacity;
    }

    // Search and remove an element if it is found in the array
    // If possible, avoid calling this method as it takes O(n) time
    bool remove(int elem) {
        for (int i = 0; i < len; i++) {
            if (arr[i] == elem) {
                removeAt(i);
                return true;
            }
        }
        return false;
    }

    // Reverse the contents of this array
    void reverse() {
        for (int i = 0; i < len / 2; i++) {
            int tmp = arr[i];
            arr[i] = arr[len - i - 1];
            arr[len - i - 1] = tmp;
        }
    }

    // Perform a binary search on this array to find an element in O(log(n)) time
    // Make sure this array is sorted! Returns a value < 0 if item is not found
    int binarySearch(int key) {
        int* result = std::lower_bound(arr, arr + len, key);
        if (result == arr + len || *result != key)
            return -1;
        return result - arr;
    }

    // Sort the array
    void sort() {
        std::sort(arr, arr + len);
    }

    // Iterator is still fast but not as fast as iterative for loop
    class Iterator {
    private:
        int* ptr;
    public:
        Iterator(int* p) : ptr(p) {}

        bool hasNext() {
            return *ptr != '\0';
        }

        int next() {
            return *ptr++;
        }
    };

    // Example usage
    friend std::ostream& operator<<(std::ostream& os, const IntArray& arr) {
        if (arr.len == 0) {
            os << "[]";
        } else {
            os << "[";
            for (int i = 0; i < arr.len - 1; i++) {
                os << arr.arr[i] << ", ";
            }
            os << arr.arr[arr.len - 1] << "]";
        }
        return os;
    }
};

int main() {
    IntArray ar(3);
    std::cout << ar.capacity << std::endl;
    std::cout << ar.len << std::endl;
    ar.add(3);
    ar.add(7);
    std::cout << "Capacity: " << ar.capacity << std::endl;
    std::cout << "Length: " << ar.len << std::endl;
    ar.add(69);
    std::cout << "Capacity: " << ar.capacity << std::endl;
    std::cout << "Length: " << ar.len << std::endl;
    ar.add(-21);
    ar.add(-69);
    ar.add(283);
    std::cout << "Capacity: " << ar.capacity << std::endl;
    std::cout << "Length: " << ar.len << std::endl;
    ar.add(33);
    ar.capacity = 20;
    std::cout << "Capacity: " << ar.capacity << std::endl;

    // ar.sort();

    // for(int i=0; i<ar.size(); i++)  std::cout << ar.get(i) << std::endl;

    std::cout << ar << std::endl;

    return 0;
}
