'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''


# Brute Force: Use 2 loops, check condition and break once satisfied. 
# If the current element is bigger than target, then skip that --> this logic only works if all numbers in the array are positive
# also using the condition: continue if arr[i] >= target, skips the possibility that a number can be added to 0 to get the same number as target.
# but if we have a combination of both positive and negative numbers than we need to do the standard double loop without skipping

# def two_sum_brute(arr: list[int], target: int) -> list[int]:
#     n = len(arr)
#     for i in range(n):
#         if arr[i] >= target:
#             continue
#         for j in range(i+1, n):
#             if arr[i] + arr[j] == target:
#                 return [i, j]
    
# TC: O(n**2), SC: O(1)
def two_sum_brute(arr: list[int], target: int) -> list[int]:
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return [i, j]


# Optimal Soltion: Make use of a hashmap. Start iterating the array and look for the required value i.e. req = target - arr[i],
# if it exists then return [i, index(req)]. 
# If not then store the current element as key and its index as value into the hashmap, for future use.
# If the entire is array is iterated and no pair is found, then there exists no such 2 sum pairs.
# TC: O(n), SC: O(n). 
# SC O(n) because we are maintaining a hashmap of n elements, TC: O(n) because we are iterating the array once.
# Looking up a key in hashmap takes O(1) average time, worst case(very unlikely) takes O(n). Insertion takes O(1) time too.
def two_sum_opti(arr: list[int], target: int) -> list[int]:
    n = len(arr)
    mp = {}
    for i in range(n):
        req = target - arr[i]
        if req in mp:
            return [mp[req], i]
        mp[arr[i]] = i
    return []



# The so called Optimal Solution as provided in the articles of takeuforward.org for this sum is for another variant of this sum
# in which we do not need to return the indices of the pair elements, instead return true or false if they exists or not.
# Sort the array and then make use of 2 pointers, one on the left(begining) and right(end) of the array.
# If arr[left] + arr[right] > target, then decrement right, if it is < target then increment left, till sum == target, else return False
# TC: O(n) + O(n*log(n)), SC: O(1)
def two_sum_var2(arr: list[int], target: int) -> bool:
    n = len(arr)
    arr.sort()
    left = 0
    right = n-1
    while left <= right:
        if arr[left] + arr[right] == target:
            return True

        if arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    
    return False



if __name__ == "__main__":
    arr1 = [2, 11, 7, 15]
    tar1 = 9        # output: [0, 2]
    
    arr2 = [2, 6, 5, 8, 11]
    tar2 = 14       # output: [1, 3]
    
    op1_b = two_sum_brute(arr1, tar1)
    op2_b = two_sum_brute(arr2, tar2)
    
    op1_o = two_sum_opti(arr1, tar1)
    op2_o = two_sum_opti(arr2, tar2)
    
    print(f"Brute Method: \nOutput1: {op1_b}, Output2: {op2_b}")
    print()
    print(f"Optimal Method: \nOutput1: {op1_o}, Output2: {op2_o}")    
    print()
    print("Do 14 as a sum of pairs exist in arr2? -> ", two_sum_var2(arr2, 14))
    print("Do 15 as a sum of pairs exist in arr2? -> ", two_sum_var2(arr2, 15))
    print() 