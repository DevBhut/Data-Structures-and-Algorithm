
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
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Here n = size of both linked list combined

# Brute Force: Append the values of linked list one by one in an array, sort the array and create a new linked list
# TC: O(n*log(n)) -> because of sorting, SC: O(2n), one of array, another of new linked list

# Brute Force better: Append the values of linked list in the array in a merge sort fasion, ie while checking the condition of less than
# then append the values in a new linked list. TC: O(2n), SC: O(2n)

# Optimal Approach: Instead of making a new linked list, we modify the existing 2 linked list such that linking them into one and return its head.
# TC: O(n), SC: O(1)
def merge_brute(head1: Node, head2: Node) -> Node:
    head = Node(-1)
    temp = head
    while head1 and head2:
        if head1.data <= head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        temp = temp.next
    
    while head1:
        temp.next = head1
        head1 = head1.next
        temp = temp.next
    while head2:
        temp.next = head2
        head2 = head2.next
        temp = temp.next
    return head.next


def print_ll(head: Node) -> None:
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
    return


if __name__ == "__main__":
    ll1 = LinkedList()
    arr1 = [3, 5, 7]
    ll1.insert_using_arr(arr1)
    head1 = ll1.insert_at_head(1)
    ll2 = LinkedList()
    arr2 = [4, 6]
    ll2.insert_using_arr(arr2)
    head2 = ll2.insert_at_head(2)
    print("List1: ")
    ll1.print()
    print("List2: ")
    ll2.print()
    head = merge_brute(head1, head2)
    print("Sorted List: ")
    print_ll(head)
    print("Printing ll1: ")
    ll1.print()