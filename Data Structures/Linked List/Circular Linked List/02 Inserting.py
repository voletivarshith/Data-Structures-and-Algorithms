# Inserting an element in a circular linked list
"""
Inserting an element in a circular linked list can be done in 2 ways
case 1: Inserting at beginning 
case 2: Inserting at some other position
enter a position of a node that is to be inserted a position can be 0<=pos<=n
if pos>=n then it will insert at the position of pos%n
"""
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def creation(self):
        n = int(input("Enter number of element: "))
        arr = list(map(int,input("Enter the elements in an array: \n").split()))
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
    def insertion(self,head):
        pos = int(input("Enter the position of an element to be inserted: "))# Position can be 0 <= pos <= n
        ele = int(input("Enter the element to be inserted: "))
        node_to_be_inserted = Node(ele)# Create a node that is to be inserted
        if head==None:
            node_to_be_inserted.next = node_to_be_inserted
            return node_to_be_inserted
        if pos==0:# Case 1
            temp1 = head.next # Assign the temp1 as head.next node 
            temp2 = head
            node_to_be_inserted.next = head# Assign the new_node.next to the head node
            head = node_to_be_inserted# Reassign the head node
            while temp1.next!=temp2:# Traverse the node until the the last node points to the head node
                temp1 = temp1.next
            temp1.next = head # Reassign the last node next to the head node
        else:
            curr_node = head 
            for i in range(pos-1): # Traverse the nodes upto pos-1 times
                curr_node = curr_node.next
            node_to_be_inserted.next = curr_node.next# assign the node_to_be_inserted.next to the curr_node
            curr_node.next = node_to_be_inserted# Reassign the prev_node.next to the new node i.e node_to_be_inserted
        return head
    def display(self,head):
        temp = head
        while temp.next!=head:
            print(temp.data)
            temp = temp.next
        print(temp.data)
linked_list = LinkedList()
head = linked_list.creation()
head = linked_list.insertion(head)
linked_list.display(head)