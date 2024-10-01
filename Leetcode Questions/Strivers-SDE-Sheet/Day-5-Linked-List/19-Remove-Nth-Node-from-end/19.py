
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



# Brute Force: Count the length of the linked list, delete L-n+1 node (L: length), (n: nth node from end)
# TC: O(2n). SC: O(1)
def delete_n_from_back_brute(head: Node, N: int) -> Node:
    temp = head
    len = 0
    while temp:
        temp = temp.next
        len += 1
    print("Length of linked list: ", len)
    n = len - N
    if n == 0:      # deleting head condition
        temp = head
        head = temp.next
        temp.next = None
        return head
    elif n == len or n<0:
        return head
    else:
        temp = head
        for i in range(n-1):
            temp = temp.next
        temp.next = temp.next.next     
        return head
        

# Optimal: maintain 2 nodes, fast and slow. First move the fast pointer N steps ahead, and then if remaining, move both 
# fast and slow 1-1 steps untill fast reaches the final node (fast.next = None). When the fast pointer reaches the last node,
# the slow pointer is guaranteed to be at N+1 node from the back i.e slow.next = Nth node from back / node to be deleted.
# TC: O(n) as we traverse the list exactly once, SC: O(1)
def delete_n_from_back_opti(head: Node, N: int) -> Node:
    slow = head
    fast = head
    for i in range(N):
        fast = fast.next 
    if fast is None:
        return slow.next
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    temp = slow.next
    slow.next = slow.next.next 
    temp = None
    return head 



if __name__ == "__main__":
    ll = LinkedList()
    arr = [2, 3, 4, 5]
    ll.insert_using_arr(arr)
    head = ll.insert_at_head(1)
    print("Linked list: ")
    ll.print()
    new_head = delete_n_from_back_opti(head, 2)
    print("Linked list after deletion: ")
    print_ll(new_head)