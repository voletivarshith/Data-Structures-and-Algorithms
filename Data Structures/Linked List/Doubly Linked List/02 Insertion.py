# Inserting into a Doubly linked list
"""
Inserting into a doubly linked list can be done at 2 ways
Case 1: If pos is 0 then insertion
Case 2: Insertion at 1<=pos<=n-1
Case 3: Insertion at nth position
"""
class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class LinkedList:
    def creation(self):
        n = int(input("Enter the number of nodes: "))
        arr = list(map(int,input("Enter the elements:\n").split()))
        try:
            first_node = Node(arr[0])
            head = first_node
        except IndexError:
            return (None,None)
        for i in range(1,n):
            first_node.next = Node(arr[i])
            first_node.next.prev = first_node
            first_node = first_node.next
        return (head,first_node)
    def displayUsingHead(self,head):
        while head:
            print(head.data)
            head = head.next
    def displayUsingTail(self,tail):
        while tail:
            print(tail.data)
            tail = tail.prev
    def insertion(self,head):
        pos = int(input("Enter the position at which the node to be inserted: "))# pos can be 0<=pos<=n
        ele = int(input("Enter the element to be inserted: "))# Element to be inserted
        new_node = Node(ele)# Creating a new node
        if head==None:# If head is None
            return (new_node,new_node)# return new_node as head and tail
        if pos==0:# If pos is equal to 0
            new_node.next = head# assign the new_node.next to the head
            head.prev = new_node# assign the head.prev node to the new_node(previously head.prev is pointing to None now it should points to the new_node)
            head = new_node# Reassigning the head node
        else:
            curr_node = head # Assign curr_node as the head node
            for i in range(pos-1):
                curr_node = curr_node.next# Traverse the curr_node 
            new_node.next = curr_node.next# Assign the new_node.next to the curr_node.next
            curr_node.next = new_node# assign the curr_node.next to the new_node
            new_node.prev = curr_node# Assign the new_node.prev to the new_node(before new_node a node is present so new_node.prev is assigned to the curr_node)
            temp = new_node.next# Assign the temp as new_node.next
            curr_node = curr_node.next # Traverse the curr_node to the next(We are doing this to add the next_node prev pointer points to the new_node)
            if temp != None:# if temp is equal to None then there is no need to assign the prev node since the prev_node is already assigned 
                temp.prev = new_node # if temp is not None then temp.prev points to the new_node
        tail = head# Assign a variable tail to the head
        # It is optional step here I am just returning the tail node to show you traversing a doubly linked list from tail node
        while tail.next!=None:# Traversing the head node to the last to return the tail node
            tail = tail.next
        return (head,tail)
linked_list = LinkedList()
head,tail = linked_list.creation()
head,tail = linked_list.insertion(head)
linked_list.displayUsingHead(head)
print()
linked_list.displayUsingTail(tail)