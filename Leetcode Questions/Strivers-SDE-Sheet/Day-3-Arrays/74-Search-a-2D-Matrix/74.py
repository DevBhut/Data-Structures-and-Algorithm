'''
You are given an m x n integer matrix matrix with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''

# Brute Force: Parse the entire matrix taking O(n*m) time 

# Better: My Intuition: Since each row is sorted in increasing order, and the 2nd property, find the row wherein the 
# target element lies and then do a binary search on it. TC: O(n) + O(logm). O(n) to find the row in which target lies in
# O(logm) to find the target inside that row using binary search

def binarySearch(arr: list[int], target: int) -> bool:
    n = len(arr)
    l = 0
    h = n
    while l < h:
        mid = (l+h)//2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            h = mid
        elif target > arr[mid]:
            l = mid+1
    return False
            

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    row = len(matrix)
    col = len(matrix[0])
    tar_row  = -1
    for i in range(row):
        if matrix[i][0] <= target <= matrix[i][col-1]:
            tar_row = i
            break
    
    if tar_row == -1:
        return False
    
    found = binarySearch(matrix[tar_row], target)
    return found
            


# Optimal Solution: Flatten the 2-d array, and apply binary search on that taking O(log(n*m)) time
# But flattening a 2-d array will take O(n*m) time and an additional space. Therefore find a way to do this without this.
# The range of the indices of the imaginary 1D array is [0, (NxM)-1] and in this range, we will apply binary search.
# If index = i, and no. of columns in the matrix = m, the index i corresponds to the cell with 
# row = i / m and col = i % m. More formally, the cell is (i / m, i % m)(0-based indexing).
# TC: O(log(n*m)), SC: O(1)
def searchMatrixOpti(matrix: list[list[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    
    # Applying Binary Search on the entire array considering it as a 1-d array of size n*m
    l = 0
    h = n*m
    while l < h:
        mid = (l+h) // 2
        row = mid // m
        col = mid % m
        if target == matrix[row][col]:
            return True
        elif target > matrix[row][col]:
             l = mid+1
        else:
            h = mid
    return False
            
            
            
            
if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    target1 = 13
    print("Is target in matrix: ",searchMatrixOpti(matrix, 55))