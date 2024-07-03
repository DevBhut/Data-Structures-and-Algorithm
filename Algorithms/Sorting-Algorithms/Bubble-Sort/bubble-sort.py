# Bubble Sort: Compare adjacent elements and swap. At the end of each iteration the largest element is stored at the end of the array. 
# Sorts from right to left, ie. from maximum to minimum, right side of array gets sorted first. 
# Lagest element "BUBBLES OUT" to the top/end of the array.

# TC: Worst Case / Avg Case: O(n**2)
# Best Case (already sorted array): O(n) -> only needs to traverse the array once, if no swap then break the loop and return.


# In Python, integers are immutable, so swapping two integers using a function won't have any effect outside the function. 
# You need to swap elements of the list directly.
def swap(arr: list[int], i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(1, n):
        for j in range(n-i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)

    
def bubble_sort_opti(arr: list[int]) -> None:
    n = len(arr)
    didSwap = False
    for i in range(1, n):
        for j in range(n-i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                didSwap = True
        if not didSwap:
            break
   
    
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
    bubble_sort_opti(arr)
    print("Sorted Array: ")
    for i in arr:
        print(i, end=" ")
    print()