

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
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


[1, 2, 3, 2, 1]
'''


# Brute Force: Parse the linked list once and store the elemenets in a stack (so that they are stored in reverse order).
# Traverse the ll once again and check the value of elements with that in the stack, if same continue, else return False.
# TC: (2n)      SC: (n)
def ll_palindrome_brute(head: Node) -> bool:
    if not head or not head.next:
        return True
    temp = head
    st = []
    while temp:
        st.append(temp.data)
        temp = temp.next
    temp = head
    while temp:
        if temp.data != st.pop():   # Note: in this step only the element in the stack is poped, thus no need to pop again
            return False
        temp = temp.next
    return True



# Optimal Approach: Find the middle using rabbit and tortoise method, and then reverse the 2nd half of the array.
# Now iterate and check the first half and second half of the ll. Reverse the second half again to make it the original ll
# TC: O(2n) -> (n/2 + n/2 + n/2 + n/2)      SC: (1)
# TC explaination: finding middle, reversing, checking palindrome, reversing
'''
If we use the condition: while fast and fast.next: we get the middle element for ll with odd no of elements and 2nd middle element for ll with even number of elements.
Eg: [1, 2, 3, 2, 1] -> for this the slow/mid will be at 3, [1, 2, 3, 4, 2, 1] -> for this the slow/mid will be at 4.
Now for checking if palindrome, for even we will reverse the perfect second half, but for odd number of elements, we want to reverse the second half after middle element,
so that we can compare the last element with the first, second last with second and so on.. and when it comes to the middle element we can ignore it as the short half of ll will point to None.
Thus we want to start reversing from the next node pointed by mid ie mid.next. This holds true for odd number of element, but not true for even as this method gives the second middle.
In order to achieve this we need to make use of: while fast.next and fast.next.next: 

The below solution can be further optimized by reversing the first half simultaneously as we reach the middle, and then check from middle onwards (or second half) 
'''
def reverse_ll(head: Node) -> Node:
    prev = None
    temp = head
    while temp:
        front = temp.next 
        temp.next = prev
        prev = temp
        temp = front
    return prev


def ll_palindrome_opti(head: Node) -> bool:
    if not head or not head.next:
        return True
    
    temp = head
    slow = temp
    fast = temp
    
    # Getting middle 
    while fast.next and fast.next.next:
        fast = fast.next.next 
        slow = slow.next
    mid = slow

    new_head = mid.next
    head2 = reverse_ll(mid.next)
    head1 = head
    
    while head1 and head2:
        if head1.data != head2.data:
    
            # while head1.next:
            #     head1 = head1.next
            # head2 = reverse_ll(head2)
            # head1.next = head2
            # No need to do the above, as mid is already pointing to mid.next and as we reverse it, mid.next becomes the last node and points to None,
            # but mid is still pointing to mid.next, so now we just need to reverse it again so that mid.next points to the next node in ll instead of None.
            reverse_ll(new_head)
            return False

        head1 = head1.next
        head2 = head2.next
    
    reverse_ll(new_head)
    return True



if __name__ == "__main__":
    # ll = LinkedList()
    # arr = [5, 4, 3, 2, 1]
    # ll.insert_using_arr(arr)
    # head = ll.insert_at_head(6)
    # ll.print()
    # new_head = reverse_linked_list(head)
    # print_ll(new_head)
    
    ll1 = LinkedList()
    arr1 = [2, 2, 1]
    ll1.insert_using_arr(arr1)
    h1 = ll1.insert_at_head(1)
    # ll1.print()
    
    ll2 = LinkedList()
    arr2 = [2, 3, 2, 1]
    ll2.insert_using_arr(arr2)
    h2 = ll2.insert_at_head(1)
    # ll2.print()
    
    ll3 = LinkedList()
    arr3 = [2, 3, 3, 2, 1, 0]
    ll3.insert_using_arr(arr3)
    h3 = ll3.insert_at_head(1)
    # ll3.print()
    
    print("Brute: ")
    print(f"LL1: {ll_palindrome_brute(h1)}. LL2: {ll_palindrome_brute(h2)}. LL3: {ll_palindrome_brute(h3)}.")
    print()
    print("Opti: ")
    print(f"LL1: {ll_palindrome_opti(h1)}. LL2: {ll_palindrome_opti(h2)}. LL3: {ll_palindrome_opti(h3)}. ")
    
    
    
        