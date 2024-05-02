'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
'''

# My intuition, sort the intervals array first (python's in-built sort function does it wrt to the first indexed element)
# Then maintain two pointers: start and end, check condition of <=, if true then increment end pointer, if false 
# finalList.append([arr[start][0], arr[end][1]]) and start = end = i++ 

# did not work for the testcase: input = [[1,4],[2,3]],    myOutput = [[1,3]]    expectedOutput = [[1,4]]

def mergeArr(arr: list[list[int]]) -> list[list[int]]:
    n = len(arr)
    start, end = 0, 0
    final = []
    arr.sort()
    for i in range(n-1):
        if arr[i+1][0] <= arr[i][1]:
            end = i+1
        else:
            # Changes to handle the test case 
            if arr[start][1] > arr[end][1]:
                final.append([arr[start][0], arr[start][1]])
            else:
                final.append([arr[start][0], arr[end][1]])
            start = i+1
            end = i+1
    if arr[start][1] > arr[end][1]:
        final.append([arr[start][0], arr[start][1]])
    else:
        final.append([arr[start][0], arr[end][1]])
    return final
    
    
# after making the changes for the first test case, the above code did not work for testcase:
# input = [[2,3],[4,5],[6,7],[8,9],[1,10]]    myOutput: [[1,10],[4,5],[6,7],[8,9]]    expectedOutput: [[1,10]]
# Intuition: maintain a global max list storing and updating the global max value and its index 

    
# My intuition was right, but just check with the last element inside the final/output list and also take care of max of 
# end value (arr[i]["1"]) element wrt to the end value of last element in final/output
def merge(arr: list[list[int]]) -> list[list[int]]:
    n = len(arr)
    ans = []
    arr.sort()
    for i in range(n):
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    return ans 



if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals1 = [[1,3],[2,6],[8,10],[15,18],[5, 7],[11, 16]]
    intervals2 = [[1,4],[2,3]]
    intervals3 = [[2,3],[4,5],[6,7],[8,9],[4,10]]    
    print(merge(intervals))
    print(merge(intervals1))
    print(merge(intervals3))