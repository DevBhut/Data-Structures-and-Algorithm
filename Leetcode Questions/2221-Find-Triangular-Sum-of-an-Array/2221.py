

def findSum(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    while True:
        n = len(nums)
        newNums = []
        print("Nums len: ", n)
        print(nums, "\n")
        for i in range(n-1):
            newNums.append((nums[i] + nums[i+1])%10)
        nums = newNums
        
        if len(nums) == 1:
            return nums[0]
        
        
if __name__ == "__main__":
    print(findSum([1,2,3,4,5]))