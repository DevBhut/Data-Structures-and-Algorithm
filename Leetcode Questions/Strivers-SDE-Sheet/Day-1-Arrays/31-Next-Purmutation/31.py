def nextPer(arr: list[int]):
    n = len(arr)
    ind = -1
    
    for i in range(n-2, -1, -1):
        if arr[i+1] > arr[i]:
            ind = i
            break
        
    if ind == -1:
        arr.reverse()
    else:
        for i in range(n-1, ind, -1):
            if arr[i] > arr[ind]:
                arr[i], arr[ind] = arr[ind], arr[i]
                break
        arr[ind+1 : ] = reversed(arr[ind+1 : ])
        

if __name__ == '__main__':
    arr = [2, 1, 5, 4, 3, 0, 0]
    nextPer(arr)
    print("Next Permutation is: ")
    for i in arr:
        print(i, end=" ")
        