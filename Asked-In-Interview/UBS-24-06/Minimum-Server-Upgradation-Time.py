'''
Given two servers and the time taken to upgrade each server in seconds, denoted by t1 and t2 respectively, in one second,
only one server undergoes the upgrade process. The severs recieve requests at certain time intervals and pause upgrades 
during those seconds. The servers recieve requests at multipes of req1 and req2 respectively. 
Determine the minimum total time (in seconds) required to upgrade both servers.

Example 1:
t1 = 3      req1 = 2
t2 = 1      req2 = 3
Output: 
5.
Server 1 will upgrade at the 1st, 3rd and 5th second, whereas Server 2 will upgrade at 2nd second

Ig the logic was correct, but had time exceeded warning. Passed 2 use cases out of 10. 
'''



def min_upgrade_time(t1: int, req1: int, t2: int, req2: int) -> int:
    time = 1
    t1-=1
    #time += 1
    while True:
        time += 1
        if time % req1 != 0 and t1>0:
            t1 -= 1
            #time += 1
        elif time % req2 != 0 and t2>0:
            t2 -= 1
            #time += 1
        if t1==0 and t2==0:
            break
        # time += 1
        
    return time
    



if __name__ =="__main__":
    time = min_upgrade_time(3, 2, 1, 3)
    print(time)