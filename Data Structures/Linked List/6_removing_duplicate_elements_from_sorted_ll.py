# Removing duplicate elements from sorted linked list
"""
Approch by using 2 pointers
assign the ele value as curr_node.data
assign the prev_node as the first_node
assign the curr_node as the first_node.next 
Iterate until the curr_node value is None
check if node data is equal to the next node data
if equal modify then change the prev_node.next to curr_node.next so i.e ignoring the curr_node
else change the ele value as the curr_node.data and reassign the prev node to the curr_node we are changing only the prev node because the prev_node should move to the next as the next element data is not equal.
at last move the curr_node to the next_node
"""
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def creation(self):
        n = int(input("Enter the number of nodes: "))
        arr = list(map(int,input("Enter the elements:\n").split()))
        try:
            curr_node = Node(arr[0])
            head = curr_node
        except IndexError:
            return None
        for i in range(1,n):
            curr_node.next = Node(arr[i])
            curr_node = curr_node.next
        return head
    def display(self,head):
        while head:
            print(head.data)
            head = head.next
    def removeDuplicateElements(self,head):
        curr_node = head
        ele = curr_node.data
        prev_node = curr_node
        curr_node = curr_node.next
        while curr_node:
            if ele == curr_node.data:
                prev_node.next = curr_node.next
            else:
                ele = curr_node.data
                prev_node = curr_node
            curr_node = curr_node.next
        return head

linked_list = LinkedList()
head = linked_list.creation()
linked_list.display(linked_list.removeDuplicateElements(head))