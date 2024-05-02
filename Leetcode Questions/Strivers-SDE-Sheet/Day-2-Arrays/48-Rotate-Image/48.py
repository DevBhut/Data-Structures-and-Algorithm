'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
'''


# Brute Force. Time Complexity: O(n**2), Space Complexity: O(n**2) ie extra space 
def rotateImageBrute(arr: list[list[int]]) -> list[list[int]]:
    n = len(arr)
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = arr[i][j]
    # or copy into the same arr and do not return anything, will take an additional O(n**2) time for copying
    return rotated          


# Optimal: Take Transpose of the Matrix and reverse the elements in each row. Time Complexity: O(n**2), Space Complexity: O(1)
def rotateImageOpti(arr: list[list[int]]) -> list[list[int]]:
    n = len(arr)
    # Transposing the Matrix
    for i in range(n):
        for j in range(i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    # Reversing each row
    for i in range(n):
        arr[i].reverse()
    return arr

if __name__ == '__main__':
    matrix1 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print("Matrix1 before roatatiing: ")
    for i in matrix1:
        print(i)
    print("Matrix1 after rotating: ")
    matrix1 = rotateImageBrute(matrix1)
    for i in matrix1:
        print(i)
    print(" ")
    print("Matrix2 before rotating: ")
    for i in matrix2:
        print(i)
    print("Matrix2 after rotating: ")
    rotateImageOpti(matrix2)
    for i in matrix2:
        print(i)