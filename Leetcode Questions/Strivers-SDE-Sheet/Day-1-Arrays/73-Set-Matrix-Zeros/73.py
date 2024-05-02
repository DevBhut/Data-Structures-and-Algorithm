# only optimized code here. Rest all approaches in cpp

def makeZeros(matrix: list[list[int]]) -> list[list[int]]:
    col = 1
    m = len(matrix)
    n = len(matrix[0])
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j!=0:
                    matrix[0][j] = 0
                else:
                    col = 0
                    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
     
    # change the 1st row first            
    if matrix[0][0] == 0:
        for j in range(n):
            matrix[0][j] = 0
    
    # now change the col
    if col == 0:
        for i in range(m):
            matrix[i][0] = 0

            
            

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
makeZeros(matrix)
print("Matrx after transformation: ")
for row in matrix:
    for i in row:
        print(i, sep="\t", end=" ")
    print()
    