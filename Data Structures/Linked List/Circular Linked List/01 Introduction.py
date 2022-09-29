# Introduction to Circular linked list
# Displaying the circular linked list
"""
A circular linked list is also a singly linked list but the last node in the circular linked list points to the head node
if there is only one head node then the last node points to the itself 
Creating a circular linked list is same as creating a singly linked list just at last assigning the lastnode next to the head node 
"""

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def creation(self):
        n = int(input("Enter the number of nodes: "))
        arr = list(map(int,input("Enter the elements in a linked list:\n").split()))
        try:
            first_node = Node(arr[0])
            head = first_node
        except IndexError:
            return None
        for i in range(1,n):
            first_node.next = Node(arr[i])
            first_node = first_node.next
        first_node.next = head
        return head
    def display(self,head):
        temp = head
        while temp!=head.next:
            print(head.data)
            head = head.next
        print(head.data)
    def displayUsingRecursion(self,head):
        if head!=self.temp or self.flag == 0:
            self.flag = 1
            print(head.data)
            head = head.next
            return self.displayUsingRecursion(head)
linked_list = LinkedList()
head = linked_list.creation()
linked_list.display(head)
linked_list.temp = head
linked_list.flag = 0