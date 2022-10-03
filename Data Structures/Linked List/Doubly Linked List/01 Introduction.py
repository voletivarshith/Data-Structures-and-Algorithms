# Doubly Linked List
"""
In doubly linked list the node will points to the next node and prev node 
so for first node the prev node is None since there is no node before the first node
for last node the next is none since there is no node after the last node
"""
class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class LinkedList:
    def creation(self):
        n = int(input("Enter number of nodes: "))
        arr = list(map(int,input("Enter the elements: \n").split()))
        try:
            curr_node = Node(arr[0])
            head = curr_node
        except IndexError:
            return None
        for i in range(1,n):
            new_node = Node(arr[i])# Creating a node
            curr_node.next = new_node# assign the curr_node.next with the newly created node
            new_node.prev = curr_node# assign the new_node.prev to the curr_node
            curr_node = curr_node.next# Traverse the curr_node to the next node
        return (head,curr_node)
    def displayUsingHead(self,head):
        while head:
            print(head.data)
            head = head.next
    def displayUsingTail(self,tail):
        while tail:
            print(tail.data)
            tail = tail.prev
linked_list = LinkedList()
head,tail = linked_list.creation()
linked_list.displayUsingHead(head)
print()
linked_list.displayUsingTail(tail)