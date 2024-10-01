'''
Not on leetcode. Link: https://www.naukri.com/code360/problems/count-inversions_615

 Given an array of N integers, count the inversion of the array.

What is an inversion of an array? 
Definition: for all i & j < size of array, 
if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].
Return the number of such pairs.

Example 1:
Input Format: N = 5, array[] = {1,2,3,4,5}
Result: 0
Explanation: 
we have a sorted array and the sorted array has 0 inversions as for i < j you will never find a pair such that A[j] < A[i]. 
More clear example: 2 has index 1 and 5 has index 4 now 1 < 5 but 2 < 5 so this is not an inversion.

Example 2:
Input Format: N = 5, array[] = {5,4,3,2,1}
Result: 10
Explanation: 
we have a reverse sorted array and we will get the maximum inversions as for i < j we will always find a pair such that A[j] < A[i]. 
Example: 5 has index 0 and 3 has index 2 now (5,3) pair is inversion as 0 < 2 and 5 > 3 which will satisfy out conditions and for reverse sorted array we will get maximum inversions and that is (n)*(n-1) / 2.For above given array there is 4 + 3 + 2 + 1 = 10 inversions.

Example 3:
Input Format: N = 5, array[] = {5,3,2,1,4}
Result: 7
Explanation: 
There are 7 pairs (5,1), (5,3), (5,2), (5,4),(3,2), (3,1), (2,1) and we have left 2 pairs (2,4) and (1,4) as both are not satisfy our condition. 
'''


# Brute Force Sol:  2 loops, 1 count variable. Increment count if condition satisfies
# TC: O(n**2)   SC: O(1)
def count_inversions_brute(arr: list[int]) -> int:
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
    return count 


# Optimal: Modification in merge operation of merge sort
# TC: O(n*log(n))   SC: O(n)
def merge(arr: list[int], low: int, mid: int, high: int) -> int:
    temp = []
    left = low
    right = mid+1
    
    count = 0     # Modification -> mainting a count variable
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
            count += (mid - left + 1)     # mid + 1 = left half of the array, reducing so far left from it 
            # The left and right half are sorted while doing this step, so if an element(e1) in the left subarr is 
            # greater than any element(e2) in right subarr, then all elements in the right of e1 will be greater than e1, 
            # since the left subarr is sorted. and thus all the elements towards right of e1 (which are greather than e1),
            # will form a pair with e2. Thus adding mid - left + 1 to count 
    
    while left <= mid:
        temp.append(arr[left])
        left += 1 
    
    while right <= high:
        temp.append(arr[right])
        right += 1
        
    for i in range(low, high+1):
        arr[i] = temp[i-low]
        
    return count


def merge_sort(arr: list[int], low: int, high: int) -> int:
    count = 0
    if low >= high:
        return count
    mid = (low + high) // 2
    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid+1, high)
    count += merge(arr, low, mid, high)
    return count 


def count_inversions_opti(arr: list[int]) -> int:
    n = len(arr)
    return merge_sort(arr, 0, n-1) 
            
    


if __name__ == "__main__":
    arr1 = [3, 2, 1]        #output: 3
    arr2 = [5, 3, 2, 1, 4]  #output: 7
    output1 = count_inversions_opti(arr1)
    output2 = count_inversions_opti(arr2)
    print(f"Output1: {output1}. Output2: {output2}")