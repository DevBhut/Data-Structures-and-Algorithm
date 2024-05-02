'''
Not on leetcode. Link: https://www.naukri.com/code360/problems/873366
a list of size n contains 1-n numbers, with exactly one number being repeated. Return the repeated and the missing number

Example 1
Input:[3 1 2 5 3] 
Output:[3, 4]. Here 3 is repeated and 4 is missing

Follow Up
Can you do this in linear time and constant additional space? 
'''

# Brute Force: maintain a hash map/list/array. TC: O(n), SC: O(n)
def missingRepeat(arr: list[int]) -> tuple[int, int]:
    n = len(arr)
    count = [[0, 0]]*(n+1)     # numbers from 1 to n will take index from 1 to n (ignoring the index 0 as 0 is not in the input list)
    for i in range(n):
        count[i][0] += 1
        count[i][1] = 1
    count.sort()
    
    