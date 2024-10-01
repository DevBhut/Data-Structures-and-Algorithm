'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

'''
cannot declare a set of tuples, i.e. st = {()}
It works fine when the set is empty, giving output as [[]] (after ans = [list(quads)for quads in st])
But if we have quads. then an extra empty list is also present in ans 
'''



# Brute Force: make use of 4 loops, sorting the quadruples and storing in a set 
# TC: O(n**4)   SC: O(2* no of unique quadruples)
def four_sum_brute(arr: list[int], target: int) -> list[list[int]]:
    n = len(arr)
    st = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    sum = arr[i] + arr[j]
                    sum += arr[k] + arr[l]
                    if sum == target:
                        temp = [arr[i], arr[j], arr[k], arr[l]]
                        temp.sort()
                        st.add(tuple(temp))
                        
    if not st:
        return [[]]
    ans = [list(quads)for quads in st]
    return ans 



# Better Solution: Similar to three sum, but instead of two make use of three pointers and 
# look up for the req value in the hash, store the values in hash as the third pointer progresses.
# TC: O[(n**3) * log(M)), M = no of elements in the set   SC: O(2*no of quads) + O(n)
def four_sum_better(arr: list[int], target: int) -> list[list[int]]:
    n = len(arr)
    st = set()
    for i in range(n):
        for j in range(i+1, n):
            mp = set()
            for k in range(j+1, n):
                req = target - (arr[i] + arr[j] + arr[k])
                if req in mp:
                    temp = [arr[i], arr[j], arr[k], req]
                    temp.sort()
                    st.add(tuple(temp))
                mp.add(arr[k])
                
    if not st:
        return [[]]
    
    ans = [list(quads) for quads in st]
    return ans



# Optimal Solution: Similar to three sum, but instead of 1 fixed and 2 moving pointers, 
# we will have 2 fixed and 2 moving pointers.
# TC: O(n**3) + O(n*log(n))   SC: O(no of quads) -> but only to return and not for processing/operations
def four_sum_opti(arr: list[int], target: int) -> list[list[int]]:
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if i!=0 and arr[i] == arr[i-1]:
            continue
        
        for j in range(i+1, n):
            if j!=i+1 and arr[j] == arr[j-1]:
                continue
            
            # 2 variable/moving pointers
            k = j+1
            l = n-1
            
            while k<l:
                sum = arr[i] + arr[j] + arr[k] + arr[l]
                if sum == target:
                    ans.append([arr[i], arr[j], arr[k], arr[l]])
                    k+=1
                    l-=1
                
                    while k<l and arr[k] == arr[k-1]:
                        k+=1
                    while k<l and arr[l] == arr[l+1]:
                        l-=1
                
                elif sum < target:
                    k+=1
                else:
                    l-=1
    
    if not ans:
        return [[]]
    
    return ans



if __name__ == "__main__":
    arr1 = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]    # Output: [[1 1 3 4 ] [1 2 2 4 ] [1 2 3 3 ]]
    target1 = 9
    
    arr2 = [0, 2, 3, -4, -6, 7, 10, 16, -14]     # Output: [[]]
    target2 = 40
    
    o1_br = four_sum_brute(arr1, target1)
    o1_be = four_sum_better(arr1, target1)
    o1_op = four_sum_opti(arr1, target1)
    
    o2_br = four_sum_brute(arr2, target2)
    o2_be = four_sum_better(arr2, target2)
    o2_op = four_sum_opti(arr2, target2)
    
    print(f"Array1: \nBrute: {o1_br}\nBetter: {o1_be}\nOpti: {o1_op}\n\n")
    print(f"Array2: \nBrute: {o2_br}\nBetter: {o2_be}\nOpti: {o2_op}\n\n")
    
    

'''
Codes of other users:

Code1:

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        def twoSum(nums, target, curComb):
            L, R = bisect_left(nums, target - nums[-1]), bisect_right(nums, target - nums[0])-1

            while L < R:
                left, right = nums[L], nums[R]
                if left + right == target:
                    res.append(curComb + [left, right])
                    L += 1
                    while L < R and nums[L-1] == nums[L]:
                        L += 1
                    R-=1
                    while R > L and nums[R+1] == nums[R]:
                        R -=  1
                    R = bisect_right(nums, target - nums[L])-1
                elif left + right < target:
                    L += 1
                    while L < R and nums[L-1] == nums[L]:
                        L += 1
                    R = bisect_right(nums, target - nums[L])-1
                    L = bisect_left(nums, target - nums[R])
                elif left + right > target:
                    R -= 1
                    while R < L and nums[R+1] == nums[R]:
                        R -=  1
                    L = bisect_left(nums, target - nums[R])
                    R = bisect_right(nums, target - nums[L]) - 1
                
        def nSum(nums, target, k, curComb):
            for i, n in enumerate(nums[:-k+1]):
                if i > 0 and n == nums[i-1]:
                    continue
                curComb += [n]
                if k > 3:
                    nSum(nums[i+1:], target-n, k-1, curComb)
                else:
                    twoSum(nums[i+1:], target-n, curComb)
                if curComb:
                    curComb.pop()
            
            return res
        
        nSum(nums, target, 4, [])

        return res
        

Code2:

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []

            # If we have run out of numbers to add, return res.
            if not nums:
                return res

            # There are k remaining values to add to the sum. The
            # average of these values is at least target // k.
            average_value = target // k

            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1 :], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)

            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1

            while lo < hi:
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (
                    hi < len(nums) - 1 and nums[hi] == nums[hi + 1]
                ):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

            return res

        nums.sort()
        return kSum(nums, target, 4)
        
'''