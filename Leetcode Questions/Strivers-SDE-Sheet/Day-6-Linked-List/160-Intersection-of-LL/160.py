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


from typing import Optional, Union
'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

Example 1:
Input:
    List 1 = [1,3,1,2,4], List 2 = [3,2,4]
Output:
    2
Explanation: Here, both lists intersecting nodes start from node 2.

Example 2:
Input:
    List1 = [1,2,7], List 2 = [2,8,1]
Output:
    Null
Explanation: Here, both lists do not intersect and thus no intersection node is present.
'''
# We can not compare wrt to the value stored in the Linked List as one value may be same in both the linked list, but that
# may not be the intersection point. 
# We need to compare the node of the linked list itself, as node is a reference or pointer to the memory location,
# i.e. when we do print(node), we get the memory location of the node and thus we can use this to compare,
# i.e. the intersection node will have the same memory location value.

# n: size of list1    m: size of list2

# Brute Force Solution: run two loops, comparing values. TC: O(n*m), SC: O(1)
def find_intersection_brute(head1: Node, head2: Node) -> Optional[Node]:
    while head2:
        temp = head1
        while temp:
            if temp == head2:
                return head2
            temp = temp.next
        head2 = head2.next
    return None


# Better Solution: Hashing, store the values of all the nodes(memory location) of any one list to a hashmap, and then
# for the second list, check if that node includes in the hashmap, return the first occurence. 
# Using hash cause hash for 2 values is always different.
# TC: O(m+n)    SC: O(n) or O(m) depending on which list is being hashed    
def find_intersection_better(head1: Node, head2: Node) -> Optional[Node]:
    st = set()
    temp = head1
    while temp:
        st.add(temp)
        temp = temp.next
    temp = head2
    while temp:
        if temp in st:
            return temp
        temp = temp.next
    return None


# Optimal Solution 1: find the length of both the list, subtract bigger - smaller and move the head of the bigger list 
# to the difference value. The compare the nodes of both the list and move both the lists simultaneously. 
# TC: O(2m) + O(m-n) + O(n) -> m: max len of two, n: min len of two.    SC: O(1)
def find_intersection_opti1(head1: Node, head2: Node) -> Optional[Node]:
    temp1 = head1
    temp2 = head2
    len1 = 0
    len2 = 0
    while temp1 or temp2:
        if temp1:
            len1 += 1
            temp1 = temp1.next
        if temp2:
            len2 += 1
            temp2 = temp2.next
            
    temp1 = head1
    temp2 = head2
    
    if len1 == len2:
        temp1 = head1
        temp2 = head2
    elif len1 > len2:
        dif = len1 - len2
        for i in range(dif):
            temp1 = temp1.next
    else:
        dif = len2 - len1
        for i in range(dif):
            temp2 = temp2.next
    
    while temp1 and temp2:
        if temp1 == temp2:
            return temp1
        temp1 = temp1.next
        temp2 = temp2.next
    
    return None


# Optimal Soltion 2: Take two dummy nodes for each list. Point each to the head of the lists. Iterate over them.
# If anyone becomes null, point them to the head of the opposite lists and continue iterating until they collide.
# TC: O(2*m), m: len of bigger list (Reason: Uses the same concept of difference of lengths of two lists).  SC: O(1)
def find_intersection_opti2(head1: Node, head2: Node) -> Optional[Node]:
    temp1 = head1 
    temp2 = head2
    while temp1 != temp2:
        temp1 = head2 if temp1 == None else temp1.next
        temp2 = head1 if temp2 == None else temp2.next
    return temp1 


if __name__ == "__main__":
    com = Node(5)
    com.next = Node(7)
    x = Node(2)
    x.next = Node(3)
    x.next.next = com
    y = Node(4)    
    y.next = com
    print("List1: ")
    print_ll(x)
    print("List2: ")
    print_ll(y)
    
    # # Non intersecting
    # x_ = LinkedList()
    # y_ = LinkedList()
    # x_.insert_using_arr([3, 5, 7])
    # x_ = x_.insert_at_head(2)
    # y_.insert_using_arr([7, 9])
    # y_ = y_.insert_at_head(4)
    # print("List1: ")
    # print_ll(x_)
    # print("List2: ")
    # print_ll(y_)
    
    brute = find_intersection_brute(x, y)
    better = find_intersection_better(x, y)
    opti1 = find_intersection_opti1(x, y)
    opti2 = find_intersection_opti2(x, y)
    print("Brute: ", brute.data if brute!=None else None)
    print("Better: ", better.data if better!=None else None)
    print("Opti1: ", opti1.data if opti1!=None else None)
    print("opti2: ", opti2.data if opti2!=None else None)
    
            
        




