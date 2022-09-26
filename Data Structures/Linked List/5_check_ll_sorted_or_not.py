# Checking whether the linkedlist is sorted or not
"""
Logic
Each element should be greater than or equal to the previous element
let us assume that the first previous element is some -ve value
assume that each node data is positive value
"""
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def creation(self):
        n = int(input("Enter the number of nodes: "))
        arr = list(map(int,input("Enter the elements in a linked list: \n").split()))
        try:
            head = Node(arr[0])
            first_node = head
        except IndexError:
            return None
        for i in range(1,n):
            first_node.next = Node(arr[i])
            first_node = first_node.next
        return head
    def display(self,head):
        while head:
            print(head.data)
            head = head.next
    def check_sorted_or_not(self,head):
        min = -1
        while head:
            ele = head.data
            if ele>min:
                min = ele
            else:
                return False
            head = head.next
        return True
linked_list = LinkedList()
head = linked_list.creation()
print(linked_list.check_sorted_or_not(head))