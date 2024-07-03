# Selection Sort: Select minimum and swap. Sorts from left to right, ie. from minimum to maximum.
# For a given index 'i', swap it with the smallest value in the array starting from 'i+1'

#TC: All Case: O(n**2)



# In Python, integers are immutable, so swapping two integers using a function won't have any effect outside the function. 
# You need to swap elements of the list directly.
def swap(arr: list[int], i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i, n):
            if arr[j] < arr[mini]:
                mini = j
        swap(arr, mini, i)
    
    
def create_arr() -> list[int]:
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    print("Enter the elements of array: ")
    for i in range(n):
        arr.append(int(input()))
    print()
    print("The array is: ")
    for i in arr:
        print(i, end="")
    print()
    return arr
    
    
if __name__ == "__main__":
    arr = create_arr()
    selection_sort(arr)
    print("Sorted Array: ")
    for i in arr:
        print(i, end="")
    print()