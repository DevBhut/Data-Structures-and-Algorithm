'''
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000
'''


# Brute Force: Loop till n and keep multipling x. TC: O(n), SC: O(n)
def powBrute(x: float, n: int) -> float:
    ans = 1.0
    nn = n
    if nn < 0:
        nn = nn*(-1)
    for i in range(n):
        ans = ans * x
    if n < 0:
        ans = 1 / ans
    return ans


# Optimal Solution: For odd n, do ans = ans * x, n--; for even n, do x = x * x, n//2 (this makes the loop to become binary)
# TC: O(log n), SC: O(1)
def powOpti(x: float, n: int) -> float:
    ans = 1.0
    nn = n
    if nn < 0:
        nn = nn*(-1)
    while nn:
        if nn % 2 == 0:
            x = x * x
            nn = nn // 2
        else:
            ans = ans * x
            nn = nn - 1
    if n < 0:
        ans = 1 / ans
    return ans



if __name__ == '__main__':
    print(powBrute(2.0, 10))
    print(powOpti(3.0, 5))