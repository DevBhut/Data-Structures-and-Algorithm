'''
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits it has (also known as the Hamming weight).
Constraints: 1 <= n <= 231 - 1

Follow up: If this function is called many times, how would you optimize it?

'''

# Method 1 (String):
def hm(n: int):
    n_b = bin(n)
    w = 0
    for ele in n_b:
        if ele == '1':
            w+=1
    return w

# Method 2 (String): 
# def hm(n: int):
#     return bin(n).count('1') 

# Method 3 : Bit Manipulation, see C++ sol

n = 356
print(hm(n))

   

