'''
Not on leetcode. Link: https://www.naukri.com/code360/problems/873366
a list of size n contains 1-n numbers, with exactly one number being repeated. Return the repeated and the missing number

Example 1
Input:[3 1 2 5 3] 
Output:[3, 4]. Here 3 is repeated and 4 is missing

Follow Up
Can you do this in linear time and constant additional space? 
'''


# Brute Force: run the loop twice, first loop selecting an element, second loop checking whehter that element is repeated again or is missing.
# TC: O(n**2), SC: O(1) (only using two int variables)

def missingRepeatBrute(arr: list[int]) -> tuple[int, int]:
    n = len(arr)
    repeat, missing = -1, -1
    
    for i in range(1, n+1):             # since numbers in arr are from 1 to n
        count = 0
        for j in range(n):
            if arr[j] == i:
                count += 1
        if count == 2:
            repeat = i
        elif count == 0:
            missing = i
        if repeat != -1 and missing != -1:
            break
    
    return [repeat, missing]
    
    

# My Brute Force (Better sol): maintain a hash map/list/array. TC: O(n), SC: O(n)
def missingRepeatBetter(arr: list[int]) -> tuple[int, int]:
    n = len(arr)
    hash = [0] * (n+1)
    
    # Update hash
    for i in range(n):
        hash[arr[i]] += 1
        
    # Find repeating and missing number, start from 1 to n+1 (as hash includes 0 index as well)
    repeat, missing = -1, -1
    for i in range(1, n+1):
        if hash[i] == 2:
            repeat = i
        elif hash[i] == 0:
            missing = i
        if repeat != -1 and missing != -1:
            break
    
    return [repeat, missing]






if __name__ == '__main__':
    input1 = [3, 1, 2, 3, 5]
    print(missingRepeatBetter(input1))
    
    
    