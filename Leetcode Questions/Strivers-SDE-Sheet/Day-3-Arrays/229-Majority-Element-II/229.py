'''
Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Example 1:
    Input: nums = [3,2,3]    Output: [3]
Example 2:
    Input: nums = [1]    Output: [1]
Example 3:
    Input: nums = [1,2]    Output: [1,2]
'''


# Note: for 3, there will be only 2 elements that appear more than ⌊ n/3 ⌋ times.
# Proof: [1, 1, 1, 2, 2, 2, 3, 3, 3] -> n=9, n//3=3. None of the elements occur more than 3 times. Can relate to mod operation
# Similarly for 4, there will be only 3 majority elements 

# Brute Force: maintain two loops, first one selecting element, second one counting its occurence.
# TC: O(n^2), SC: O(1)
def majorityBrute(arr: list[int]) -> list[int]:
    n = len(arr)
    ele = set()
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count > n//3:
            ele.add(arr[i])
    return list(ele)



# Better1: Sort and count. TC: O(n*logn), SC: O(1)
def majorityBetter1(arr: list[int]) -> list[int]:
    n = len(arr)
    # Need to do this since we do not check the last element. 
    if n < 3:
        return list(set(arr))  
    arr.sort()
    ele = set()
    count = 1
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            count += 1
        elif arr[i] != arr[i+1]:
            count = 1
        if count > n//3:
            ele.add(arr[i])
            if len(ele) == 2:
                return list(ele)



# Better2: Make use of a hashmap. TC: O(n), SC: O(n)
from collections import Counter
def majorityBetter2(arr: list[int]) -> list[int]:
    ele = []
    n = len(arr)
    counter = Counter(arr)
    for num, count in counter.items():
        if count > n//3:
            ele.append(num)
    return ele 


     
# Optimal Solution: Extended Moore's Voting Algorithm. Since for > n//3, we will have only 2 majority elements.
# Thus we maintain 2 element variable and their respective counters, ie 4 variables, ele1, cnt1, ele2, cnt2. 
# After the loop ends, ele1 and ele2 are our majority elements. TC: O(n), SC: O(1)
def majorityOpti(arr: list[int]) -> list[int]:
    ele1, ele2, cnt1, cnt2 = float('-inf'), float('-inf'), 0, 0
    n = len(arr)
    for i in range(n):
        if cnt1 == 0 and ele2 != arr[i]:
            ele1 = arr[i]
            cnt1 += 1
        elif cnt2 == 0 and ele1 != arr[i]:
            ele2 = arr[i]
            cnt2 += 1
        elif arr[i] == ele1:
            cnt1 += 1
        elif arr[i] == ele2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
            
    ele = []
    # Check whether the elements stored in ele1 & ele2 are majority elements
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if arr[i] == ele1:
            cnt1 += 1
        if arr[i] == ele2:
            cnt2 += 1
    if cnt1 > n//3:
        ele.append(ele1)
    if cnt2 > n//3:
        ele.append(ele2)
    
    # Sort the answer array if the question requires
    # if len(ele) == 2 and ele[0] > ele[1]:
    #     ele[0], ele[1] = ele[1], ele[0]
    
    return ele        



if __name__ == "__main__":
    print(majorityBetter1([1, 2, 3, 1, 3, 2, 1, 2]))
    print(majorityOpti([1, 2, 3, 1, 3, 2, 1, 2, 1, 1, 1]))