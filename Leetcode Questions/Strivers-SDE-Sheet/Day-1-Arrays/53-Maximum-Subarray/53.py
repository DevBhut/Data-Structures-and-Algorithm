'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''
import sys


# Brute Force Solution, make use of 3 loops: one for starting index of subarray, second for ending index
# of subarray and third to take the summation of the subarray
# Time Complexity: O(n**3)
def maxSubArrBrute(arr: list[int]) -> int:
    n = len(arr)
    maxi = -sys.maxsize - 1
    
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j+1):
                sum += arr[k]
            maxi = max(maxi, sum)
    # check for empty subarray, ie if maxi = -ve, we return sum=0, ie of empty subarray
    if maxi < 0:
        maxi = 0
    return maxi


# Better Solution, in Brute Force, instead of running the last loop to calculate the sum, do it the 2nd loop
# Time Complecity: O(n**2)
def maxSubArrBetter(arr: list[int]) -> int:
    n = len(arr)
    maxi = -sys.maxsize - 1
    
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            maxi = max(maxi, sum)
    if maxi < 0:
        maxi = 0
    return maxi



# Optimized Solution, Make use of single loop. Maintain two variables: sum and maxi like above, but if sum<0: sum = 0 
# ie reinitialise sum as 0 if it becomes negative, cause -ve sum will never lead to maximum subarr sum
# Time Complexity: O(n)
def maxSubArrOpt(arr: list[int]) -> int:
    n = len(arr)
    maxi = -sys.maxsize - 1
    sum = 0
    
    for i in range(n):
        sum += arr[i]
        maxi = max(maxi, sum)
        if sum<0:
            sum = 0
    if maxi<0:
        maxi = 0 
    return maxi


# Additional: Also print the subarray
def maxSubArrPrint(arr: list[int]) -> tuple[list[int], int]:
    n = len(arr)
    maxi = -sys.maxsize - 1
    sum = 0
    start, end = -1, -1
    
    for i in range(n):
        if sum == 0:
            start = i
        sum += arr[i]
        if sum > maxi:
            maxi = sum
            end = i
        if sum<0:
            sum = 0
    if maxi<0:
        maxi = 0
        sub = []
    else:   
        sub = arr[start:end+1]
    return maxi, sub
            


if __name__ == '__main__':
    arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum Subarray Sum: ", maxSubArrBrute(arr))
    print("Maximum Subarray Sum: ", maxSubArrBetter(arr))
    print("Maximum Subarray Sum: ", maxSubArrOpt(arr))
    print("Maximum Subarray Sum: ", maxSubArrPrint(arr))


    