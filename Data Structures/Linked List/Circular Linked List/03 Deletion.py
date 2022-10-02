# Deleting a node in a circular linked list
"""
Deleting a node in a linked list
Deleting a node can be done at 2 positions
Case 1: Deleting a node at 1st position
Case 2: Deleting a node at other position
0<=pos<=n-1
"""
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def creation(self):
        n = int(input("Enter number of nodes: "))
        arr = list(map(int,input("Enter the elements:\n").split()))
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
        while temp.next!=head:
            print(temp.data)
            temp = temp.next
        print(temp.data)
    def deletion(self,head):
        pos = int(input("Enter the position of the node to be deleted: "))# Pos can be 0<=pos<=n-1 
        temp = head # Assign the temp variable as head node
        if pos==0: # Case 1
            temp = temp.next # change the temp variable to the next position since the first_node is to be deleted
            temp1 = head # Assign the temp1 as the head node to delete the first_node
            head = head.next # Traverse the head node to the next node since we need to delete the first node
            while temp.next!=temp1: # Here we are checking the last node i.e last node points to the first node so we are checking the last node
                temp = temp.next # Traversing
            temp.next = head # Finally temp points to the last node so reassign the temp.next to the head node(head node points to the 2nd node in the linked list) and we have removed the 1st node from the list
        else:# Case 2
            for i in range(pos-1):# Traverse the node upto pos-1 times
                temp = temp.next
            temp.next = temp.next.next# Reassign the temp.next to the temp.next.next i.e we are neglecting the temp.next node
        return head
linked_list = LinkedList()
head = linked_list.creation()
linked_list.display(linked_list.deletion(head))