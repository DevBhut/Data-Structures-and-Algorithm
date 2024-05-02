import sys

def minSubArr(arr: list[int]) -> int:
    n = len(arr)
    sum = 0
    mini = sys.maxsize
    for i in range(n):
        sum += arr[i]
        mini = min(mini, sum)
        if sum > 0:
            sum = 0
    return mini

if __name__ == "__main__":
    arr = [-2, 1, -3, -3, -1, 10, 2, 1, -5, -4]
    print("Array: ", arr)
    print("Minimum Sub of Subarray: ", minSubArr(arr))