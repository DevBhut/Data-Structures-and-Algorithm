'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]       Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]       Output: 2

[1, 1, 1, 2, 2, 2, 2]
'''




# Brute Force: maintain two loops, first one selecting element, second one counting its occurence.
# TC: O(n^2), SC: O(1)
def majorityBrute(arr: list[int]) -> int:
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
            if count > (n/2):
                return arr[i]
            

# My Approach: sort [O(n*logn)] the numbers in the array first and count [O(n)] their occurance,
# break loop when count > n/2 and return that element. TC: O(n*logn), SC: O(1)
def majorityBetter1(arr: list[int]) -> int:
    n = len(arr)
    arr.sort()
    count = 1
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            count += 1
        elif arr[i] != arr[i+1]:
            count = 1
        if count > n/2:
            return arr[i]
    
    
# Better Approach, make use of hash map -> takes O(n*log(n)) time to store an element, and another loop for 
# searching which takes O(n) time. TC: O(n*logn), SC: O(n) -> maintaing a hash map
from collections import Counter
def majorityBetter2(arr: list[int]) -> int:
    n = len(arr)
    counter = Counter(arr)
    for num, count in counter.items():
        if count > n/2: 
            return num
    

# Optimal Approach: Moore's Voting Algorithm, helps count the majority element by counting majority element and
# minorities (minority elements grouped together). TC: O(n), SC: O(1)
# [2, 2, 1, 1, 1, 2, 2] -> in this if the last two elements are 3 then the element variable will store 3 and we 
# need to run another loop to check whether the stored element is the majority element or not, if the question guarantees 
# that the given array contains a majority element then we do not need to run the 2nd loop again. 
def majorityOpti(arr: list[int]):
    n = len(arr)
    count = 0
    ele = None
    for i in range(n):
        if count == 0:
            count = 1
            ele = arr[i]
        elif ele == arr[i]:
            count += 1
        else:
            count -= 1
    
    # Checking if the stored element is the majority element
    cnt = 0
    for i in range(n):
        if arr[i] == ele:
            cnt += 1
    if cnt > n/2:
        return ele
    return -1


if __name__ == "__main__":
    print(majorityOpti([2,2,1,1,1,2,2]))
    print(majorityOpti([3, 1, 3]))
    print(majorityOpti([-8, 2, -9, 0, 2, 8, 34, 2, 0, -8, 2, 2, 2, 2, 2]))