'''
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:
0 <= i < j < nums.length and
nums[i] > 2 * nums[j].

Example 1:
Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

Example 2:
Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
 
'''



# Brute Force: Iterate twice, check condition and store it in a list or tuple
# TC: O(n**2)    SC: O(n**2) [At worst, all possible pairs are reverse pairs] (if using tuple). 
# SC: O(1). If we use a counter variable
def reverse_pairs_brute(nums: list[int]) -> int:
    n = len(nums)
    pairs = set()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > 2*nums[j]:
                pairs.add((i, j))
                count += 1
    return count



# Optimal: Modification in merge operation of merge sort. 
# Same as count inversions but, include a count_pairs function which returns the count of the condition 
# arr[i]>2*arr[j] before merging the sorted sub-arrays. 
# TC: O(2n*log(n))    SC: O(n)
# TC: 2n -> because the function count_pairs takes 'n' TC; log(n) for divide/merge, n for sorting, another n for condition checking.

# The count_pairs function, which checks the condition of arr[i]>2*arr[j] or n times for generalized case
def count_pairs(arr: list[int], low: int, mid: int, high: int) -> int:
    count = 0
    right = mid + 1
    for i in range(low, mid+1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        count += (right - (mid + 1))
    return count


def merge(arr: list[int], low: int, mid: int, high: int):
    temp = []
    left = low
    right = mid + 1
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(low, high+1):
        arr[i] = temp[i-low]
        

def merge_sort(arr: list[int], low: int, high: int) -> int:
    count = 0
    if low >= high:
        return count
    mid = (low + high) // 2
    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid+1, high)
    # Counting the valid pairs before the standard merge operation 
    count += count_pairs(arr, low, mid, high)
    # Normal merge operation
    merge(arr, low, mid, high)
    return count


def reverse_pairs_opti(arr: list[int]) -> int:
    n = len(arr)
    return merge_sort(arr, 0, n-1)
    


if __name__ == "__main__":
    arr1 = [1, 3, 2, 3, 1]      # output = 2
    arr2 = [2, 4, 3, 5, 1]      # output = 3
    arr3 = [4, 1, 2, 3, 1]      # output = 3
    output1 = reverse_pairs_opti(arr1)
    output2 = reverse_pairs_opti(arr2)
    output3 = reverse_pairs_opti(arr3)
    print(f"Output1: {output1}. Output2: {output2}. Output3: {output3}")