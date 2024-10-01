
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
    
    

'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
'''

def find_middle(head: Node) -> Node:
    rabbit = head
    tortoise = head
    while rabbit and rabbit.next:
        rabbit = rabbit.next.next
        tortoise = tortoise.next
    return tortoise


if __name__ == "__main__":
    ll = LinkedList()
    arr = [5, 4, 2, 1, 4]
    ll.insert_using_arr(arr)
    head = ll.insert_at_head(3)
    print("Linked List:")
    ll.print()
    middle = find_middle(head)
    print("Middle value: ", middle.data)