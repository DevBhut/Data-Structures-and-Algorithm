'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
'''


# Brute Force: square all elements and then sort. TC: O(nlog(n)), SC: O(1)

# Optimal: My Intuition: find the separation(sep) index from where the positive numbers start, maintain two pointers;
# one to the left of sep and another to the right of sep. Iterate the left and right pointers while comparing the elements,
# squaring and appending them to new list/array
# TC: O(n), SC: O(n)

def sortedSquares(arr: list[int]) -> list[int]:
    n = len(arr)
    sep = -1
    final = []
    
    for i in range(n):
        if arr[i] >= 0:
            sep = i
            break
    
    if sep == -1:          # ie all negative numbers in given array
        arr.reverse()
        final = [x**2 for x in arr]
        return final
    
    left = sep - 1
    right = sep
    
    while left >=0 and right < n:
        if arr[right] < abs(arr[left]):
            final.append((arr[right])**2)
            right += 1
        else:
            final.append((arr[left])**2)
            left -= 1
    
    while left >= 0:                    # to check if any elements are left or not
        final.append((arr[left])**2)
        left -= 1
    
    while right < n:                    # to check if any elements are left or not
        final.append((arr[right])**2)
        right += 1
        
    return final
    
    
    
# Making use of two poiniters, append from the back of the final array ie checking for greater than condition. Another solution
def sortedSquares1(arr: list[int]) -> list[int]:
    n = len(arr)
    final = [0]*n
    start, end = 0, n-1
    for i in range(n-1, -1, -1):
        if abs(arr[start]) >= abs(arr[end]):
            final[i] = arr[start]**2
            start += 1
        else:
            final[i] = arr[end]**2
            end -= 1
    return final
    
    
    
    
if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    nums1 = [-7,-3,2,3,11]
    print(sortedSquares1(nums1))