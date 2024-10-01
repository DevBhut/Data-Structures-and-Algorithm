'''
Not on leetcode. https://www.interviewbit.com/problems/subarray-with-given-xor/

Given an array of integers A and an integer B.
Find the total number of subarrays having bitwise XOR of all elements equals to B.

Problem Constraints
1 <= length of the array <= 105
1 <= A[i], B <= 109

Example Input
Input 1:
A = [4, 2, 2, 6, 4]
B = 6
Output: 4
Explaination:  The subarrays having XOR of their elements as 6 are: [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
 
 
Input 2:
A = [5, 6, 7, 8, 9]
B = 5
Output: 2
Explaination: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]

'''


'''
Learnt something: 
dict: Raises KeyError when accessing a missing key. You have to handle default values manually.
defaultdict: Automatically initializes missing keys with a default value, making it more convenient in cases where you expect to frequently access non-existing keys.
More at the end

in C++, the normal map and unordered_map inserts default value (depending on the data type), ie 0 for int
'''

from collections import defaultdict

# Brute Force: Maintain two loops, considering every possible subarray.
# TC: O(n)  SC: O(1)
def count_subarrays_brute(arr: list[int], k: int) -> int:
    n = len(arr)
    count = 0
    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor ^= arr[j]
            if xor == k:
                count += 1
    return count



# Optimal Solution: XOR properties: a^b = b^a. if a^b = k(what we want),
# if the XOR of every element till index j is a, then we find b in the hashmap (i.e we find a^k = b).
# Now along with the XOR'ed value, we store its occurence in the hashmap, and add it in our count. 
# We store (0,1) (XOR value 0 occuring once) before hand, because k^k = 0
# TC: O(n)  SC: O(n)
def count_subarrays_opti(arr: list[int], k: int) -> int:
    n = len(arr)
    count = 0
    mp = defaultdict(int)
    xor = 0
    mp[xor] = 1
    for i in range(n):
        xor ^= arr[i]
        y = xor ^ k
        if y in mp:
            count += mp[y]
        mp[xor] += 1
    return count



if __name__ == "__main__":
    arr1 = [4, 2, 2, 6, 4]
    k1 = 6                  # output: 4
    arr2 = [5, 6, 7, 8, 9]
    k2 = 5                  #output: 2
    arr3 = [4, 2, 6, 6]
    k3 = 6
    
    o1_br = count_subarrays_brute(arr1, k1)
    o2_br = count_subarrays_brute(arr2, k2)
    o3_br = count_subarrays_brute(arr3, k3)
    
    o1_op = count_subarrays_opti(arr1, k1)
    o2_op = count_subarrays_opti(arr2, k2)
    o3_op = count_subarrays_opti(arr3, k3)
    
    print(f"Brute: Output1: {o1_br}, Output2: {o2_br}, Output3: {o3_br}")
    print(f"Opti: Output1: {o1_op}, Output2: {o2_op}, Output3: {o3_op}")
    
    
    
'''
Difference between default dict and dict:

In Python, defaultdict (from the collections module) and dict are both types of dictionaries, but they have some important differences in how they handle missing keys. Here's a breakdown of the differences:

1. Handling Missing Keys:
Normal dict: If you try to access a key that does not exist, it raises a KeyError.
  d = {}
  print(d['missing_key'])  # Raises KeyError
  
defaultdict: Automatically assigns a default value to a missing key, based on a specified factory function (like int, list, set, etc.). The default value is created by calling the factory function when the key is first accessed.
  from collections import defaultdict
  dd = defaultdict(int)
  print(dd['missing_key'])  # Returns 0 (default for `int`)
  
2. Default Value Initialization:
Normal dict: You must manually check for the key or handle missing keys using methods like get() or setdefault().
  d = {}
  value = d.get('missing_key', 0)  # Returns 0 if the key is missing
  
defaultdict: The defaultdict automatically initializes missing keys with a default value based on the factory provided. No need for explicit checking.
  dd = defaultdict(list)
  dd['new_key'].append(1)  # Automatically initializes `new_key` with an empty list, then appends 1
  
3. Custom Default Values:
Normal dict: You have to explicitly set a default value for each key using either the setdefault() method or handling it manually.
  d = {}
  d.setdefault('key', []).append(1)  # Appends 1, initializing with an empty list if key is missing
  
defaultdict: You specify the type (or a custom factory) when creating the dictionary, and it will use this to initialize missing keys automatically.
  dd = defaultdict(lambda: 100)
  print(dd['new_key'])  # Returns 100 (from the custom lambda)
  
4. Performance:
Normal dict:
If you're frequently checking for keys and manually setting default values, performance may be slightly slower due to repeated lookups and condition checks.

defaultdict:
Performance can be better in scenarios where missing keys are frequently accessed because the initialization and lookup of missing keys are streamlined.

5. Use Cases:
Normal dict:
Suitable when you need more control over the exact handling of missing keys or when missing keys are rare.

defaultdict:
Ideal for scenarios where missing keys are common, and you want to avoid manual key checking, such as counting frequencies or grouping items by keys.

  dd = defaultdict(int)
  for char in 'abcabc':
      dd[char] += 1  # Automatically initializes missing keys with 0, then increments
      
Summary:
dict: Raises KeyError when accessing a missing key. You have to handle default values manually. 
defaultdict: Automatically initializes missing keys with a default value, making it more convenient in cases where you expect to frequently access non-existing keys.

'''