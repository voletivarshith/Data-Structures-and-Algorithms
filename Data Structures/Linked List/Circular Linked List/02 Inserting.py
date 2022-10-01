# Inserting an element in a circular linked list
"""
Inserting an element in a circular linked list can be done in 2 ways
case 1: Inserting at beginning 
case 2: Inserting at some other position
enter a position of a node that is to be inserted a position can be 1<=pos<=n
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
        pos = int(input("Enter the position of an element to be inserted: "))
        ele = int(input("Enter the element to be inserted: "))
        node_to_be_inserted = Node(ele)# Create a node that is to be inserted
        if head==None:
            node_to_be_inserted.next = node_to_be_inserted
            return node_to_be_inserted
        if pos==1:# Case 1
            temp1 = head # Assign the temp1 as head
            node_to_be_inserted.next = head# Assign the new_node.next to the head node
            head = node_to_be_inserted# Reassign the head node
            temp_node = head.next.next# Here we can also assign the node_to_be_inserted.next.next 
            # assign the temp_node as head.next.next as the temp_node.next is points to the previous head
            # node so the while loop condition will becomes false and it will not enter into the while loop so assign head.next.next   
            while temp1!=temp_node.next:# Traverse the node until the the last node points to the old head node 
                temp_node = temp_node.next
            temp_node.next = head # Reassign the last node next to the new head node
        else:
            curr_node = head 
            for i in range(pos-1): # Traverse the nodes upto pos-1 times
                prev_node = curr_node
                curr_node = curr_node.next
            node_to_be_inserted.next = curr_node# assign the node_to_be_inserted.next to the curr_node
            prev_node.next = node_to_be_inserted# Reassign the prev_node.next to the new node i.e node_to_be_inserted
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