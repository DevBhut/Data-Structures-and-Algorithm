'''
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target 
by rotating mat in 90-degree increments, or false otherwise.

Example 1:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
'''


# Intuition: Making using of 48.py's code to rotate a matrix by 90degree, we rotate the given matrix by 90
# and check whether it is equal to target, if yes we return true, else false
# We only rotate 3 times, as the 4th 90 degree rotation will be the same as the starting matrix
# Also firstly we will check the number of 0s and 1s in the given and target matrix, if true then proceed forward
# Since it is a binary arr, ie consisting of only 0's and 1's we only need to count one of them, if we get 0's equal
# in both the array, then 1's will also be equal only

def rotate90(arr: list[list[int]]):
    n = len(arr)
    # Transposing the Matrix
    for i in range(n):
        for j in range(i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    # Reversing each row
    for i in range(n):
        arr[i].reverse()


def checkRotate(mat: list[list[int]], target: list[list[int]]) -> bool:
    mat0, target0 = 0, 0
    n = len(mat)
    
    if mat == target:
        return True
    
    for i in range(n):
        mat0 += mat[i].count(0)
        target0 += target[i].count(0)
    
    if mat0!=target0:
        return False 
    
    for i in range(3):
        rotate90(mat)
        if mat == target:
            return True
    
    return False



# Another Solution (found in leetcode solution): check each element's all 4 rotation ie 0, 90, 180, 270 degree rotation
# all at once while iterating the matrix once. Making use of 48.py's brute force 90 degree flip logic
# Optimized as we run the loop of O(n**2) time complexity only once
def checkRotateOpti(mat: list[list[int]], target: list[list[int]]) -> bool:
    check = [True]*4
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j] != target[i][j]:   check[0] = False            #  0 degree rotation check
            if mat[i][j] != target[n-j-1][i]:   check[1] = False        # 90 degree rotation check
            if mat[i][j] != target[n-i-1][n-j-1]:   check[2] = False    #180 degree rotation check
            if mat[i][j] != target[j][n-i-1]:   check[3] = False        #270 degree rotation check
    return True if True in check else False


if __name__ == "__main__":
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    target = [[1,1,1],[0,1,0],[0,0,0]]
    mat1 = [[0,1],[1,1]]
    target1= [[1,0],[0,1]]
    mat2 = [[0,0],[1,0]]
    target2 = [[1,0],[0,0]]

    print(checkRotateOpti(mat2, target2))
    
    