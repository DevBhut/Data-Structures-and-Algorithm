'''
Given an integer numRows, return the first numRows of Pascal's triangle.
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Output type: List[List[int]]

      1       --> 1
     1 1      --> 2
    1 2 1     --> 3
   1 3 3 1    --> 4
  1 4 6 4 1   --> 5
 1 5 10 10 5 1  --> 6
 
To the same leetcode question we can have 3 variations:
Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal's triangle --> (5,3) --> 6
Variation 2: Given the row number n. Print the n-th row of Pascal's triangle --> n=5 --> 1 4 6 4 1
Variation 3: Given the number of rows n. Print the first n rows of Pascal's triangle --> above output for n=6
'''

# # My method to leetcode question / variation 3: 
# # BruteForce takes O(r*r) time complexity and an additional O(r) space complexity
# # where r is the row number
# def pas_tri(numRows: int):
#     pt = []
#     if numRows == 1:
#         return [[1]]
#     elif numRows == 2:
#         return [[1], [1, 1]]
#     else:
#         pt.append([1])
#         pt.append([1, 1])
        
#         for i in range(2, numRows):
#             temp = [0]*(i+1)
#             temp[0], temp[i] = 1, 1
#             for j in range(1, i):
#                 temp[j] = pt[i-1][j] + pt[i-1][j-1]
#             pt.append(temp)
#         return pt 
# print(pas_tri(6))
        
        
# # Solution to variation 1: (Striver's solution) Making use of nCr formula
# def nCr(n: int, r: int):
#     # n = rows, r = cols
#     res = 1
#     for i in range(r):
#         res = res * (n-i)
#         res = res // (i+1)
#     return res
# # for row 5, col 3, we give the input as 4,2 as the index starts from 0
# print(nCr(5-1,3-1))


# Solution to variation 2: (Striver's solution) --> prev_element * (n-i) // i  i goes from (0,n)
def pas_row(n: int):
    ans = 1
    row = [ans]
    for i in range(1, n):
        ans = ans * (n-i) // i
        row.append(ans)
    return row
# print(pas_row(9))  


# Solution to variation 3: (Striver's solution) --> makes use of row generating function 
# This solution is similar to mine. I just make use of prev rows elements to do the typical pascal addition
# Striver's solution doesn't need any info on prev row. But the time complexity of both is same. ie both runs 2 for loops
def pas_tri_2(numRows: int):
    pt = []
    for i in range(1, numRows+1):
        pt.append(pas_row(i))
    return pt
print(pas_tri_2(6))