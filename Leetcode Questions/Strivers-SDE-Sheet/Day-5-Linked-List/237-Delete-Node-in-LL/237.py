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
There is a singly-linked list head and we want to delete a node `node` in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node `node` is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
'''


# Solution: in the given node (del), that is to be deleted; store the value of the next node and point del to next of next
# this stores the value of del.next into del, deleting the del.next node while also replacing the value of del
def delete_node(node: Node) -> None:
    temp = node.next
    node.data = temp.data
    node.next = temp.next 
    temp = None
    return 


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_using_arr([2, 5, 6, 1, 3, 8])
    print("Linked List: ")
    ll.print()
    node = ll.find(1)
    delete_node(node)
    print("Linked List after deleting node: ")
    ll.print()

