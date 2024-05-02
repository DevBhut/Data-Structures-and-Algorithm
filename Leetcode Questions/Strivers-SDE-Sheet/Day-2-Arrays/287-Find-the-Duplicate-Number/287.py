'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [3,1,3,4,2]
Output: 3

Example 2:
Input: nums = [3,3,3,3,3]
Output: 3

All the integers in nums appear only once except for precisely one integer which appears two or more times.
'''

# Brute Force, iterate and append the count value in dictionary or another array. Space Complexity: O(n), TC: O(n)
def findDuplicateBrute(arr: list[int]) -> int:
    n = len(arr)
    count = [0]*(n+1)
    for i in range(n):
        count[arr[i]] += 1
        if count[arr[i]] == 2:
            return arr[i]


# Brute Force 1, sort the array first. TC: O(nlog(n)), SC: O(1)
def findDuplicateBrute1(arr: list[int]) -> int:
    arr.sort()
    for i in range(len(arr)):
        if arr[i] == arr[i+1]:
            return arr[i]
        
        
        
# Optimal Solution: Make use of two pointers, fast and slow. Fast pointer traverse the array twice as fast as slow does
# ie in increments of 2. The place where the both pointers meet, or point to the same value, from there we move/reset 
# the fast pointer to be index 0, increment both fast and slow by one index and the index where they meet, that element is
# the repeating number. This sol makes use of the concept of a circle being formed as there is a repeat value present in the list
# Here we make use of the element value, or the numbers in the list for indexing.
# TC: O(n), since we travelled through the array once. SC: O(1)
def findDuplicateOpti(arr: list[int]) -> int:
    slow, fast = arr[0], arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    fast = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
        
    return slow
        
    
     

if __name__ == '__main__':
    nums = [3,1,3,4,2]
    nums1 = [3,3,3,3,3]
    print(findDuplicateOpti(nums))
    print(findDuplicateOpti(nums1))