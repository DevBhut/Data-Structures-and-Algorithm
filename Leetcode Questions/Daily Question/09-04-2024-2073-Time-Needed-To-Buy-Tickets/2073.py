# tickets = [2,3,2]     k = 2    time = 6 (o/p)
# tickets = [5,1,1,1]   k = 0    time = 8
# only optimized code in cpp

# Brute Force. Time: O(sum(list))
def timeReqToBuy(tickets: list[int], k: int) -> int:
    time = 0
    while True:
        for i in range(len(tickets)):
            if tickets[i] == 0:   continue
            tickets[i] -= 1
            time += 1
            if tickets[k] == 0:
                return time


# Optimised. One Pass Sol. Time: O(n)
def timeReqToBuy1(tickets: list[int], k: int) -> int:
    time = 0
    for i in range(len(tickets)):
        t = 1 if i>k else 0
        time += min((tickets[k] - t), tickets[i])
    return time   
    '''
    here we are doing tickets[k] - 1 for i>k for the condition where tickets[k] == tickets[i]
    ie to stop counting when tickets[k] becomes 0
    for ex: in tickets = [2, 7, 5, 5, 5, 3] and k = 3 we have 5 "5" 5 (for i=2,3,4) ie neighbouring value same as tickets[k]
    in such condition the value before index k will be counted as whole or here as 5(for i=2), as it needs to take ticket before our target ie k=3
    for i>k=3 or here i=4, we take min(5-1, 5) (applying condition) because i=3 wala 5 becomes 0 before i=4 wala 5 and there's no need to run the loop further
    and hence we take min of tickets[k]-1, tickets[i] to not count and extra loop 
    '''


print(timeReqToBuy([2, 7, 5, 5, 5, 3], 3))          
print(timeReqToBuy1([2, 7, 5, 5, 5, 3], 3))          

