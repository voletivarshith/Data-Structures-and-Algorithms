#Deletion of node in a linked list at a given postion
"""
Input 
n is no of elements in a linked list
arr = list of elements 
pos is the position at which the element is to be deleted assuming that pos lies between 0 to n
Deletion of node can be taken place in 2 places
Case 1 At the starting of a linked list
Case 2 At the middle
Approch 
if case 1 move the head pointer towards the next pointer
case 2 By using two pointers
1 curr node
2 prev node
curr node is the node in which it is currently pointing to and the prev node is the node which is present at the back of curr node 
iterate this process until pos-1 no of times so that the curr_node is pointing to the deleting node and the prev node is at the back of curr node 
assign the address of prev node address to the curr node.next
"""
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def creation(self):
        n = int(input("Enter the number of nodes: "))
        arr = list(map(int,input("Enter the number of elements:\n").split()))
        try:
            head = Node(arr[0])
            first_node = head
        except:
            return None
        for i in range(1,n):
            first_node.next = Node(arr[i])
            first_node = first_node.next
        return head
    def display(self,head):
        while head:
            print(head.data)
            head = head.next
    def deletion(self,head,pos):
        curr_node = head
        if pos==1:
            return head.next
        for i in range(pos-1):
            prev_node = curr_node
            curr_node = curr_node.next
        prev_node.next = curr_node.next
        return head
linked_list = LinkedList()
head = linked_list.creation()
pos = int(input("Enter the node to be deleted: "))
linked_list.display(linked_list.deletion(head,pos))
