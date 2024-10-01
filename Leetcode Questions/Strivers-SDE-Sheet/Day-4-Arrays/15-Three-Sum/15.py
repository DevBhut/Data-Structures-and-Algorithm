'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.


Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.


Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
 
Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


# Brute Force: Triple Loop. TC: O[(n**3) * (log(no. unique triplets))] -> n**3 for 3 loops and log(no. unique triplets) -> inserting into sets
# SC: O(2*no. of unique triplets) -> storing into set and list for return
# Sort the triplet pairs as we find, to store them in a set to avoid duplicates.
def three_sum_brute(arr: list[int]) -> list[list[int]]:
    n = len(arr)
    st = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    st.add(tuple(temp))
    
    if not st:
        return []
    
    ans = [list(triplets) for triplets in st]
    return ans 


# Better Solution: Making use of a hashmap and reducing to two loops
# Make use of 2 pointers as loops, and find the third required element by looking up into the hashmap and 
# storing the elements into hashmap as j progresses. Hashmap only stores the elements between i and j for that iteration of i.
# This gives us all the possible triplets that can be formed by the element maintained by first loop / pointer 'i'
# Empty the hashmap after every iteration of first loop, store into list, sort and put into a set
# TC: O[n**2 * (log(no. unique triplets))] -> same as above, just reduced one loop.
# SC: O(2*no. of unique triplets) + O(n) -> hashmap/set + set + list. (set is also a hashmap)
def three_sum_better(arr: list[int]) -> list[list[int]]:
    n = len(arr)
    st = set()
    for i in range(n):
        mp = set()
        for j in range(i+1, n):
            req = -(arr[i] + arr[j])
            if req in mp:
                temp = [arr[i], arr[j], req]
                temp.sort()
                st.add(tuple(temp))
            mp.add(arr[j])
    
    if not st:
        return []
    
    ans = [list(triplets) for triplets in st]
    return ans



# Optimal Solution: Sort the array first and make use of three pointers: i(left), k(right), j(moves between i and k)
# i is fixed, ie does not move and only moves for the iterating outer loop.
# j moves towards the right (if the sum < 0), and k moves towards the left (if the sum > 0). 
# Stop the inside loop once j and k crosses each other. Thus forming every triplets possible by 'i'
# Also continue/skip all pointers if the same element occurs in the next iteration, thus avoiding duplicates and eleminating the use of set or hashmap.
# Since we have sorted the array, the triplets formed are also in sorted order.
# TC: O(n**2) + O(n*log(n)) (for sorting),  SC: O(no. of unique triplets) -> for returning as answer (can be considered as O(1) as it is for returning and not for internal operation)
def three_sum_opti(arr: list[int]) -> list[list[int]]:
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        
        if i!=0 and arr[i] == arr[i-1]:
            continue        # skipping the same elements for i
        
        j = i+1
        k = n-1
        
        while j<k:
            sum = arr[i] + arr[j] + arr[k]
            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            else:
                temp = [arr[i], arr[j], arr[k]]
                ans.append(temp)
                j += 1
                k -= 1
                while(j<k and arr[j] == arr[j-1]):    # skipping the same elements if theres after updating j
                    j += 1
                while(j<k and arr[k] == arr[k+1]):    # skipping the same elements if theres after updating k
                    k -= 1
    
    return ans


if __name__ == "__main__":
    arr1 = [-1, 0, 1, 2, -1, -4]    # Output: [[-1,-1,2],[-1,0,1]]
    arr2 = [0, 2, 3, -4, -6, 7]     # Output: []
    
    o1_br = three_sum_brute(arr1)
    o1_be = three_sum_better(arr1)
    o1_op = three_sum_opti(arr1)
    
    o2_br = three_sum_brute(arr2)
    o2_be = three_sum_better(arr2)
    o2_op = three_sum_opti(arr2)
    
    print(f"Array1: \nBrute: {o1_br},   Better: {o1_be},   Opti: {o1_op}\n\n")
    print(f"Array2: \nBrute: {o2_br},   Better: {o2_be},   Opti: {o2_op}\n\n")