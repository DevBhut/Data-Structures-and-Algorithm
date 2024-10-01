'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''


# 0, 0, 1, 1, 2, 3, 4, 6, 7, 8


# Brute Force: For each element(x) in the array, find if x+1 exists, if yes then look for x+2, x+3, and so on...
# We do this for each element of the array, by making use of two loops, the outer loop checks consecutive sequence for each element
# and the inner loop finds the consecitve elements, ie x+1, x+2, x+3,....
# TC: O(n**2)   SC: O(1)
def linearSearch(arr: list[int], x: int) -> bool:
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return True
    return False

def longest_consecutive_brute(arr: list[int]) -> int:
    n = len(arr)
    if n == 0:
        return 0
    longest = 1
    for i in range(n):
        x = arr[i]
        curr = 1
        while linearSearch(arr, x+1):
            x += 1
            curr += 1
        longest = max(curr, longest)
    return longest



# Better Solution: Sort the array and then find the longest consecutive sequence. 
# TC: O(n*log(n)) + O(n)    SC: O(1)
def longest_consecutive_better(arr: list[int]) -> int:
    n = len(arr)
    if n == 0:
        return 0
    arr.sort()
    longest = 1
    curr = 1
    prev = arr[0]
    for i in range(1, n):
        if prev == arr[i] - 1:
            curr += 1
            prev = arr[i]
        elif prev != arr[i]:
            curr = 1
            prev = arr[i]
        longest = max(longest, curr)
    return longest



# Best Solution: Store the elements in a hashmap and instead of doing a linearSearch for the next element, 
# do direct lookup O(1) in the hashmap.
# TC: O(n) + O(2n)   SC: O(1)
def longest_consecutive_opti(arr: list[int]) -> int:
    n = len(arr)
    if n == 0:
        return 0
    longest = 1
    mp = set(arr)
    
    for ele in mp:
        if ele - 1 not in mp:       # i.e ele is the starting element of the sequence
            curr = 1
            x = ele
            while x + 1 in mp:
                x += 1
                curr += 1
            longest = max(longest, curr)
    return longest



if __name__ == "__main__":
    arr1 = [100, 4, 200, 1, 3, 2]               # output: 4
    arr2 = [0, 3, 7, 2, 5, 8, 4, -1, 6, 0, 1]   # output: 10
    
    o1_br = longest_consecutive_brute(arr1)
    o1_be = longest_consecutive_better(arr1)
    o1_op = longest_consecutive_opti(arr1)
    
    o2_br = longest_consecutive_brute(arr2)
    o2_be = longest_consecutive_better(arr2)
    o2_op = longest_consecutive_opti(arr2)
    
    print(f"Array1: Brute: {o1_br}, Better: {o1_be}, Opti: {o1_op}")
    print(f"Array2: Brute: {o2_br}, Better: {o2_be}, Opti: {o2_op}")