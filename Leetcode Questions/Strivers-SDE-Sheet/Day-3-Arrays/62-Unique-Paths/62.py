'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3

'''


# Brute Force: Recursion, recursive calling of function until condition met. 
# TC: Exponential (since we are basically trying out every possible path). SC: Exponetial (we use stack space in recursion)
def uniquePathsBrute(m: int, n: int) -> int:
    def countPathsBrute(i, j, m, n) -> int:
        if i == (m-1) and j == (n-1):
            return 1
        elif i >= m or j >=n:
            return 0
        else:
            return countPathsBrute(i+1, j, m, n) + countPathsBrute(i, j+1, m, n)
    
    return countPathsBrute(0, 0, m, n)



# Better Solution: Dynamic Programming, Maintaing a hash map (array) of the indices/places that is already visited, hence reducing the recursive calls.
# TC: O(m*n) --> At max there are m*n positions to visit at. SC: O(m*n) --> We maintain a hash table of size of m*n
# Actual SC is 2(m*n), as recusive calling will maintain a stack of the number of recursion calls made 
def uniquePathsBetter(m: int, n: int) -> int:
    
    def countPathsBetter(i, j, m, n, dp):
        if i == (m-1) and j == (n-1):
            return 1
        if i >= m or j >= n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        else:
            dp[i][j] = countPathsBetter(i+1, j, m, n, dp) + countPathsBetter(i, j+1, m, n, dp)
            return dp[i][j]
        
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    num = countPathsBetter(0, 0, m, n, dp)
    if m == 1 and n == 1:
        return num 
    return dp[0][0]

    

# Optimal Solution: Make use of nCr. I found about this method using observation, by looking at dp and pascal's triangle
# For a matrix of size m*n, the number of possible paths is (m+n-2)C(n-1). NVM, Striver's explanation better. 
# TC: O(n), SC:O(1)
def uniquePathsOpti(m: int, n: int) -> int:
    def nCr(n: int, r: int) -> int:
        # n: rows,  r: cols
        ans = 1
        for i in range(r):
            ans = ans * (n-i)
            ans = ans // (i+1)
        return ans
    return nCr(m+n-2, n-1)





if __name__ == "__main__":
    m = 3
    n = 5
    totalCount = uniquePathsOpti(m, n)
    print(f"The total number of paths for {m}x{n} matrix is: {totalCount}")    