# Quick Sort: Select a pivot randomly, place the pivot in it's correct position while simultaneously,
# sorting/storing smaller (than or equal to) elements on the left and larger elements on the right. 

# TC: O(n*log(n))   -> log to the base 2, n
# SC: O(1)          -> Not counting recursion stack space 



def swap(arr: list[int], i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
    
def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[low]
    i = low
    j = high
    while i<j:
        while arr[i]<=pivot and i<high:
            i+=1
        while arr[j]>pivot and j>low:
            j-=1
        if i<j:
            swap(arr, i, j)
    swap(arr, low, j)
    return j


def quick_sort(arr: list[int], low: int, high: int) -> None:
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)


def create_arr() -> list[int]:
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    print("Enter the elements of array: ")
    for i in range(n):
        arr.append(int(input()))
    print()
    print("The array is: ")
    for i in arr:
        print(i, end=" ")
    print()
    return arr


if __name__ == "__main__":
    arr = create_arr()
    n = len(arr)
    quick_sort(arr, 0, n-1)
    print("Sorted Array: ")
    for i in arr:
        print(i, end=" ")
    print()