'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
'''

# Brute Force, make use of an extra array. TC: O(n+m). SC: O(n+m)
def mergeSortedBrute(arr1: list[int], n: int, arr2: list[int], m: int) -> list[int]:
    i, j = 0, 0
    final = []
    while i<n and j<m:
        if arr1[i] < arr2[j]:
            final.append(arr1[i])
            i+=1
        else:
            final.append(arr2[j])
            j+=1
    while i<n:
        final.append(arr1[i])
        i+=1
    while j<m:
        final.append(arr2[j])
        j+=1
    return final


# Another Brute Force Solution I found in leetcode submissions. TC: O(nlog(n)), SC:O(1)
def mergeSortedBrute1(arr1: list[int], n: int, arr2: list[int], m: int) -> None:
    for i in range(m):
        arr1[n+1] = arr2[i]
    arr1.sort()


# Optimal Solution: 2 pointer approach. Since nums1 has extra space and is empty at the back, we iterate from behind
# and check greater than condition and update it on nums1. TC: O(m+n). SC:O(1)
def mergeSortedOpti(arr1: list[int], n: int, arr2: list[int], m: int) -> None:
    k = n+m-1
    i = n-1
    j = m-1
    while j>=0:
        if i>=0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            k-=1
            i-=1
        else:
            arr1[k] = arr2[j]
            k-=1
            j-=1



if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    n = 3
    nums2 = [2,5,6]
    m = 3
    # print(mergeSortedBrute(nums1, n, nums2, m))
    mergeSortedOpti(nums1, n, nums2, m)
    print(nums1)
    
        





