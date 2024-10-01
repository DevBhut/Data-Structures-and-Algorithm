'''
Not on leetcode. On gfg: https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Examples:
Input: arr[] = {15,-2,2,-8,1,7,10,23}, n = 8
Output: 5
Explanation: The largest subarray with sum 0 is -2 2 -8 1 7.

Input: arr[] = {2,10,4}, n = 3
Output: 0
Explanation: There is no subarray with 0 sum.

Input: arr[] = {1, 0, -4, 3, 1, 0}, n = 6
Output: 5
Explanation: The subarray is 0 -4 3 1 0.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= n <= 105
-1000 <= arr[i] <= 1000, for each valid i
'''


# Brute Force: Maintain two loops, and calculate sum. If sum == 0 update the length of longest subarray found so far.
# TC: O(n**2)   SC: O(1)
def length_0_sum_brute(arr: list[int]) -> int:
    n = len(arr)
    longest = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum == 0:
                curr_len = j-i+1
                longest = max(longest, curr_len)
    return longest



# Optimal Solution: Iterate through the array once and maintain a hashmap containing the sum so far and the index of the element.
# For any interation or current index j, if we find the same sum in the hashmap at index i, 
# then it implies that that the sum between indices j and i must me 0, as sum upto index i = k and sum upto index j = k (j>i), 
# then sum between them must be zero, we use this and update the longest length of subarray using j-i.
# Also if we already have a pair of sum, index in the hashmap and we come across a new index with the same sum, we do not update it, 
# since we want the longest subarray (i.e. keeping the smallest index of a given sum in the hashmap)
# TC: O(n) -> since we just iterate all the elements once and lookup in unordered hashmap takes o(1) time in average case
# SC: O(n)
def length_0_sum_opti(arr: list[int]) -> int:
    n = len(arr)
    mp = {}
    sum = 0
    longest = 0
    for i in range(n):
        sum += arr[i]
        if sum == 0:
            longest = i + 1
        elif sum in mp:
            longest = max(longest, i - mp[sum])
        else:
            mp[sum] = i
    return longest



if __name__ == "__main__":
    arr1 = [15, -2, 2, -8, 1, 7, 10, 23]    # output: 5
    arr2 = [2, 10, 4]                       # output: 0
    arr3 = [1, 3, 0, -5]                    # output: 1
    
    
    o1_br = length_0_sum_brute(arr1)
    o2_br = length_0_sum_brute(arr2)
    o3_br = length_0_sum_brute(arr3)
    
    o1_op = length_0_sum_opti(arr1)
    o2_op = length_0_sum_opti(arr2)
    o3_op = length_0_sum_opti(arr3)
    
    print(f"Array1: Brute: {o1_br}, Opti: {o1_op}")
    print(f"Array2: Brute: {o2_br}, Opti: {o2_op}")
    print(f"Array3: Brute: {o3_br}, Opti: {o3_op}")
    
            