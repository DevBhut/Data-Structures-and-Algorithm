'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

in-place means making changes directly on the given input data structure without requiring extra space proportional to the input size

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''


# My intuition: Iterate the loop once, keep count of 0's, 1's and 2's. Takes O(2n) time and constant space of 3 integers
# After getting the count, make changes in the original array.
def sortColors(arr: list[int]) -> list[int]:
    r, w, b = 0, 0, 0
    for color in arr:
        if color == 0:
            r += 1
        elif color == 1:
            w += 1
        else:
            b += 1
    # This is how i solved at first, not in-place solution
    # arr[ : r] = [0]*r 
    # arr[r : r+w] = [1]*w
    # arr[r+w : r+w+b] = [2]*b
    
    # In-place solution:
    for i in range(r):
        arr[i] = 0
    for i in range(r, r+w):
        arr[i] = 1
    for i in range(r+w, r+w+b):
        arr[i] = 2
        
    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# 2 Pointer Approach. In-Place Solution. Takes almost O(n) (almost cause may run a few iterations more than n)
def sortColors1(arr: list[int]) -> list[int]:
    n = len(arr)
    left = 0
    right = n - 1
    i = 0
    while i <= right:
        if arr[i] == 0:
            swap(arr, i, left)
            left += 1
            i += 1
        elif arr[i] == 2:
            swap(arr, i, right)
            right -= 1
        else: 
            i += 1
    return arr
                 

# I mistook in-place sorting with stable algorithm, hence made this function to check if it is stable or not. It is an unstable sorting algorithm
def inPlace(arr):
    n = len(arr)
    left = 0
    right = n - 1
    i = 0
    while i <= right:
        if arr[i][0] == 0:
            swap(arr, i, left)
            left += 1
            i += 1
        elif arr[i][0] == 2:
            swap(arr, i, right)
            right -= 1
        else: 
            i += 1
    return arr


if __name__ == "__main__":
    colors = [0, 1, 2, 1, 2, 0, 2, 0, 1, 2, 0]
    sortColors(colors)
    print(colors)
    colors1 = [0, 1, 2, 1, 2, 0, 2, 0, 1, 2, 0]
    sortColors1(colors1)
    print(colors1)
    # To check for stability
    # colors2 = [[0,0], [1, 1], [2, 2], [1, 3], [2, 4], [0, 5], [2, 6], [0, 7], [1, 8], [2, 9], [0, 10]]
    # print(colors2)
    # inPlace(colors2)
    # print(colors2)