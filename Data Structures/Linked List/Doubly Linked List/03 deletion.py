class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class DoubleLinkedList:
    def creation(self):#Function for creating a doubly linked list
        n = int(input("Enter the size of the linked list: "))# Enter the size of the linked list
        arr = list(map(int,input("Enter the number of elements in a double linked list: \n").split()))#Enter the elements of the double linked list
        try:
            head = Node(arr[0])#Assign the head node as the first node
            curr_node = head#Assume curr_node as the head node
        except IndexError:
            return None#if there are no elements then return None
        for i in range(1,n):
            new_node = Node(arr[i])# Create a new_node
            curr_node.next = new_node# Assign the new_node to the curr_node next node
            temp = curr_node# Store the curr_node address in a variable to assign the prev node value
            curr_node = curr_node.next# traverse the curr_node to the next location
            curr_node.prev = temp# assign the curr_node.prev value to the temp node
        return (head,curr_node)
    def traverseHeadToGetTail(self,head):
        while head.next:
            head = head.next
        return head
    def deletion(self,head):
        pos = int(input("Enter the element to be deleted: "))# Enter the position to be deleted here the position lies between the 0 to n-1
        if pos==0:
            if head==None: # If the head node is None return None
                return None
            head = head.next# reassign the head node i.e traverse the head node
            head.prev = None# assign head.prev node as the None
            return (head,self.traverseHeadToGetTail(head))
        else:
            temp1 = head
            for i in range(pos-1):# Traverse the head node to pos-1 number of times
                head = head.next
            temp = head
            if head.next.next==None:# check whether the curr_node.next.next is None if none i.e deleted node is the last element 
                head.next = None# Assign the head.next node as the None
                return (temp1,head)# return the temp1 variable i.e consisting of the head node and the tail node
            head = head.next.next# Traverse the head node to the two times 
            temp.next = head# assign the curr_node next value to the next next node
            prev_node = temp# Assign the prev_node to the temp variable 
            temp = temp.next# Traverse the temp node to the next (i.e is newly changed node)
            temp.prev = prev_node# Assign the temp.prev node to the temp 
        return (temp1,self.traverseHeadToGetTail(temp1))# return the head and the tail node
    def displayFromHead(self,head):
        if not head:# If head is None just to print the None 
            print("None")
        while head:# while head is not null
            print(head.data)# Print the node data value 
            head = head.next# Traverse the head node to the next node
    def displayFromTail(self,tail):
        if not tail:
            print("None")
        while tail:# while tail is not none
            print(tail.data)# print the value
            tail = tail.prev# traverse the tail node
ll = DoubleLinkedList()
head,tail = ll.creation()
head,tail = ll.deletion(head)
ll.displayFromHead(head)
print()
ll.displayFromTail(tail)