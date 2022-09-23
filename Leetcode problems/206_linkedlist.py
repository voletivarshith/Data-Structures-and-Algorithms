# Reversing an elements in a linked list
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def __str__(self) -> str:
        return str(self.data)
class LinkedList:
    def creation(self):
        n = int(input("Enter the number of elements: "))
        arr = list(map(int,input("Enter the elements in an array:\n").split()))
        try:
            head = Node(arr[0])
            curr_node = head
        except IndexError:
            return None
        for i in range(1,n):
            curr_node.next = Node(arr[i])
            curr_node = curr_node.next
        return head
    def display(self,head):
        while True:
            try:
                print(head.data)
                head = head.next
            except AttributeError:
                break
    def reverse(self,head):
        # first_node is having the first node address
        first_node = head # Assume first_node is head node 
        while True:
            try:
                next_node = head.next # consider the second node in a linked list
                temp_addr = next_node.next # storing the thrid node address in a temporary
                head.next = temp_addr # Assigning the next value of the node to the next value
                next_node.next = first_node #reassigning the next_node next value to the first_node 
                first_node = next_node# reassigning the first_node 
            except AttributeError:
                break
        return first_node
linked_list = LinkedList()
head = linked_list.creation()
linked_list.display(linked_list.reverse(head))

"""
Logic
1 2 3 4 5
2 1 3 4 5
3 2 1 4 5
4 3 2 1 5
5 4 3 2 1
"""