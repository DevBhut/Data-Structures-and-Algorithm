class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
        
    def insert_at_head(self, data) -> Node:
        if self.head is None:
            temp = Node(data)
            self.head = temp
            self.tail = temp
            return self.head
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        return self.head
    
    
    def insert_at_tail(self, data) -> Node:
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
            return self.tail
        self.tail.next = temp
        self.tail = temp
        return self.tail
        # Only using Head and no tail
        # if self.head is None:
        #     self.head = temp
        #     return self.head
        # last = self.head
        # while last.next:
        #     last = last.next
        # last.next = temp
        # return last.next
        
    
    def insert_using_arr(self, arr: list[int]) -> None:
        if len(arr) == 0:
            return
        
        for data in arr:
            self.insert_at_tail(data)
        return 
        
        # for i in range(len(arr)):
        #     temp = Node(arr[i])
        #     self.tail.next = temp
        #     self.tail = temp
        # return 
        # Only using Head and no tail
        # last = self.head
        # while last.next:
        #     print(last.data)
        #     last = last.next
        # print(last.data, "\n")
        # for i in range(len(arr)):
        #     temp = Node(arr[i])
        #     last.next = temp
        #     last = temp
        # return 
        
    
    def find(self, data) -> Node:
        index = 0
        temp = self.head
        while temp:
            if temp.data == data:
                print(f"{data} found at index {index}")
                return temp
            temp = temp.next
            index += 1
        print(f"{data} not found in linked list")
        return None
    
    
    def delete(self, data) -> None:
        temp = self.head
        if temp and temp.data == data:
            self.head = temp.next
            temp = None
            return 
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next
        if temp is None:
            print(f"{data} not found in linked list to delete.")
            return
        prev.next = temp.next
        if temp == self.tail:
            self.tail = prev
        temp = None
        print(f"{data} deleted from linked list.")
        return 
    
    
    def get_length(self) -> int:
        len = 0
        temp = self.head
        while temp:
            temp = temp.next
            len += 1
        return len
    
                   
    def print(self) -> None:
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        return
    
     
def print_ll(head: Node) -> None:
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
    return



'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 
Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 
Follow up: Can you solve it using O(1) (i.e. constant) memory?

'''

from typing import Optional


# Brute Force: Make use of a hashtabel/set and return the occurence of a Node.
# TC: O(n)      SC: O(n)
def detect_cycle_brute(head: Node) -> Optional[Node]:
    temp = head
    st = set()
    while temp:
        if temp in st:
            return temp
        st.add(temp)
        temp = temp.next 
    return None



# Optimal Solution: Make use of rabbit and tortoise approach to detech a cycle in the LL. 
# If cycle detected (i.e both pointers pointing to same Node), then reset slow to head and iterate till slow and fast meet and return that Node.
# TC: O(n)      SC: O(1)
def detect_cycle_opti(head: Node) -> Optional[Node]:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


if __name__ == "__main__":
    # head = [3,2,0,-4], pos = 1
    com = Node(2)
    head = Node(3)
    head.next = com
    head.next.next = Node(0)
    head.next.next.next = Node(-4)
    head.next.next.next.next = com
    # print_ll(head)        -> yeah dont do this, goes into an infite loop lmao, well now we know it works ;)
    
    head2 = Node(6)
    head2.next = Node(9)
    
    op_br = detect_cycle_brute(head)
    op_op = detect_cycle_opti(head)
    print(f"Brute: {op_br.data if op_br else None}")
    print(f"Opti: {op_op.data if op_op else None}")
    
    op2_br = detect_cycle_brute(head2)
    op2_op = detect_cycle_opti(head2)
    print(f"Brute: {op2_br.data if op2_br else None}")
    print(f"Opti: {op2_op.data if op2_op else None}")