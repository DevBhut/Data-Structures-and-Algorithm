# Insertion Sort: Insert the elements into it's correct postion.
# Compare, find the correct position, swap the elements in the array until the selected index have the correct element /
# the element is in it's correct postion. 

# TC: Worst Case / Avg Case: O(n**2)
# Best Case (already sorted array): O(n) -> only needs to traverse the array once, if no swap then break the loop and return.


# In Python, integers are immutable, so swapping two integers using a function won't have any effect outside the function. 
# You need to swap elements of the list directly.
def swap(arr: list[int], i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def insertion_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(1, n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            swap(arr, j, j-1)
            j-=1

    
def insertion_sort_opti(arr: list[int]) -> None:
    n = len(arr)
    didSwap = False
    for i in range(1, n):
        j = i
        while j>0 and arr[j-1] > arr[j]:
            swap(arr, j, j-1)
            j-=1
            didSwap = True
        if not didSwap:
            break
        print("Runs. Itr: ", i)
   
    
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
    insertion_sort_opti(arr)
    print("Sorted Array: ")
    for i in arr:
        print(i, end=" ")
    print()