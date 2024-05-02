'''
Given an integer n, return True if it is a power of two. Otherwise, return False.
Constraints: -2^31 <= n <= 2^31 - 1
'''

def isPowerOfTwo(n: int):
    if n<=0:
        return False
    else:
        # Method 1: Count Hamming Weight i.e. number of set bits, should be 1. String Method
        return 1 == bin(n).count('1')

        # Method 2: Do a bitwise AND of n and n-1, will be 0 only for n = pow of 2. Bit Manipulation Method
        # return (n & (n-1)) == 0
        
print("256 is a power of 2? -->", isPowerOfTwo(256))
print("192 is a power of 2? -->", isPowerOfTwo(192))