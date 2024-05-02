'''
A general solution for all the questions 326, 342 of leetcode, i.e power of n (n--> a +ve int)
Basically converting the integer to base n representation
Can't do the bit manipulation method of Power of 2, as for base 3, we get the output in the form of 2,1,0 
and for base 4 we get the output in the bits 3,2,1,0
Therefore making use of hamming weight 
'''

import math

# Recursive Method: 
def baseb(n: int, b: int):
    e = n//b
    q = n%b
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return baseb(e, b) + str(q)
    
    
def isPowerOf(n: int, p: int):
    if n<=0 or p<=0:    
        return False
    else:
        num = baseb(n,p)
        return num[0] == '1' and all(char == '0' for char in num[1:])
    
    
# Math Method: making use of logarithm and checking if the output is a whole number
def isPowOfMath(n: int, b: int):
    result = math.log(n, b)
    return result.is_integer()

    
print('28 in base 4 representation:', baseb(28, 4))
print('Is 28 a power of 4? -->', isPowerOf(28, 4))

    

