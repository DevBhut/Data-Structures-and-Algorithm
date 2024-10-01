'''
Given a string s, find the length of the longest substring without repeating characters.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''



# Brute Solution: Make use of two loops, one to generate substrings and other to check for the length of relevant substrings (satisfying the condition)
# Make use of a set to track the repeatation of elements.
# TC: O(n**2)   SC: O(1) -> Lets say that we only have small caps alphabets and space as characters, then the total number of unique characters = 27
# and our array length can be more that 27 cause of repeation. Thus a constant space used.
def substring_brute(arr: str) -> int:
    n = len(arr)
    if n == 0:
        return 0
    longest = 0
    for i in range(n):
        st = set()
        count = 0
        for j in range(i, n):
            if arr[j] in st:
                break
            else:
                count += 1
                longest = max(longest, count)
                st.add(arr[j])
    return longest                
    
    
    

# Better Solution: Make use of two pointers; left and right and a set. Keep moving right in a normal for loop and, 
# When a repeated element occurs, move left untill the repeated element is removed from the set, and then calculate the new length r-l+1.
# Add the element arr[r] into the set. 
# Do not empty the set as done above, instead we look for a new substring, by looking for a new value of l(i.e. starting index) 
# that will form a valid substring till r(i.e. substring end index)
# TC: O(2n)     SC: O(1)
def substring_better(arr: str) -> int:
    n = len(arr)
    if n == 0:
        return 0
    l = 0
    longest = 0
    st = set()
    for r in range(n):
        if arr[r] in st:
            while l<r and arr[r] in st:
                st.remove(arr[l])
                l += 1
        st.add(arr[r])
        longest = max(longest, r-l+1)
    return longest




# Optimal Solution: Making a sligth change in the above solution. Instead of moving l one step at a time, 
# we move l to the occurence of the repeated element, ie prev occurence of repeated element + 1 position. 
# To this we store the element and its index in a hashmap, and update the index value of the repeated element to its new postion.
# TC: O(n)      SC: O(1)
def substring_opti(arr: str) -> int:
    n = len(arr)
    l = 0
    r = 0
    longest = 0
    mp = {}
    while r < n:
        if arr[r] in mp:
            l = max(l, mp[arr[r]] + 1)
        mp[arr[r]] = r
        longest = max(longest, r-l+1)
        r += 1
    return longest

'''
if arr[r] in mp:
    1. repeating in bounds: ie l< arr[r] < r        -> move l and update new postion of arr[r]
    2. repeating but out of bound: ie arr[r] < l    -> just update the new position of arr[r]
    
in either of the two cases we need to update the position of arr[r] to r, even outside the if statement, therefore we only
need to lookout for the position of l, now this can be achieved by l = max(mp[arr[r]] + 1, l) 
i.e comparing updated position of l (ie l+1) to current position of l. 
If current position of l > arr[r] + 1 (ie prev repeat position + 1), then we do no move l and just update the new position of repeated element by simply doing mp[arr[r]] = r
and if the repeated element is in bound, then it will be greater than l (therefore making use of max solves it) and no need of if condition.

need to have if arr[r] in mp, as we are not using default dict, otherwise we will have key error.
'''



if __name__ == "__main__":
    arr1 = "abcabcbb"       # output: 3
    arr2 = "bbbb"           # output: 1
    arr3 = "pwwkew"         # output: 3
    
    o1_br = substring_brute(arr1)
    o2_br = substring_brute(arr2)
    o3_br = substring_brute(arr3)
    
    o1_be = substring_better(arr1)
    o2_be = substring_better(arr2)
    o3_be = substring_better(arr3)
    
    o1_op = substring_opti(arr1)
    o2_op = substring_opti(arr2)
    o3_op = substring_opti(arr3)
    
    
    print(f"Brute: \nOp1: {o1_br}, Op2: {o2_br}, Op3: {o3_br} \n")
    print(f"Better: \nOp1: {o1_be}, Op2: {o2_be}, Op3: {o3_be} \n")
    print(f"Opti: \nOp1: {o1_op}, Op2: {o2_op}, Op3: {o3_op} \n")
    
    