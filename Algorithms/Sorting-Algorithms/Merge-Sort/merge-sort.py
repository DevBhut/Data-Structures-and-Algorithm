# Merge Sort: Divide till an array consists of single element
# Sort while merging back up.

# TC: O(n*log(n))   -> log to the base 2, n
# SC: O(n)          -> making use of a temp array (not counting recursion stack space)

def swap(arr: list[int], i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    

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
    
    
def merge(arr: list[int], low: int, mid: int, high: int) -> None:
    temp = []
    left = low
    right = mid+1
    while left<=mid and right<=high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low, high+1):
        arr[i] = temp[i-low]


def merge_sort(arr: list[int], low: int, high: int) -> None:
    if low >= high:
        return 
    mid = (low+high)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high) 
    
   
if __name__ == "__main__":
    # arr = create_arr()
    # n = len(arr)
    arr = [9, 5, 12, -4, 3, 5]
    n = 6
    print("The array is: ")
    for i in arr:
        print(i, end=" ")
    merge_sort(arr, 0, n-1)
    print("\n\nSorted Array: ")
    for i in arr:
        print(i, end=" ")
    print()