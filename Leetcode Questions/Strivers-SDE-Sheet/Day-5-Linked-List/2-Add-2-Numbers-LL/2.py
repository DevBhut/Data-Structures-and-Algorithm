
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


def add_numbers(head1: Node, head2: Node) -> Node:
    head = Node(-1)
    temp = head
    carry = 0
    rem = 0
    while head1 and head2:
        sum = head1.data + head2.data + carry
        rem = sum % 10
        carry = sum // 10
        temp.next = Node(rem)
        temp = temp.next
        head1 = head1.next
        head2 = head2.next
    while head1:
        sum = head1.data + carry
        rem = sum % 10
        carry = sum // 10
        temp.next = Node(rem)
        temp = temp.next
        head1 = head1.next
    while head2:
        sum = head2.data + carry
        rem = sum % 10
        carry = sum // 10
        temp.next = Node(rem)
        temp = temp.next
        head2 = head2.next
    if carry != 0:
        temp.next = Node(carry)
    return head.next


# Same code, just better looking. Instead of running the loop for head1 and head2 first and then for remainging of head1 and head2 seperately,
# we do it inside one loop and check if any of them is present or not using if statements 
def add_numbers_better_looking(head1: Node, head2: Node) -> Node:
    head = Node(-1)
    temp = head
    carry = 0
    while (head1 or head2) or carry:
        sum = 0
        if head1:       # Checking if head1 is not null
            sum += head1.data
            head1 = head1.next
        if head2:       # Checking if head2 is not null
            sum += head2.data
            head2 = head2.next
        if carry:
            sum += carry
        carry = sum // 10
        temp.next = Node(sum%10)
        temp = temp.next
    return head.next
            
    
    
    


if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.insert_using_arr([4, 3])
    head1 = ll1.insert_at_head(2)
    ll2.insert_using_arr([6, 8, 9])
    head2 = ll2.insert_at_head(5)
    # ll1.insert_using_arr([9,9,9,9,9,9])
    # head1 = ll1.insert_at_head(9)
    # ll2.insert_using_arr([9,9,9])
    # head2 = ll2.insert_at_head(9)
    print("Linked List1: ")
    ll1.print() 
    print("Linked List2: ")
    ll2.print()
    print("Linked List after addition: ")
    new = add_numbers_better_looking(head1, head2)
    print_ll(new)