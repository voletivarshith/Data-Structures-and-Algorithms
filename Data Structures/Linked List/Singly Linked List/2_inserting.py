class LinkedList:
    def inserting(self,head,index,element):# index at which index the element should be inserted , element which element to be inserted
        # Assuming the index starts from 1
        # So if index is 1 then inserting the node at first
        # If index is n+1 then inserting the node at last
        curr_node = head
        new_node = Node(element) # Creating a new node 
        if index == 0:
            new_node.next = curr_node # Assigning new node next as curr_node since the index is 1 so new_node.next is head node
            return new_node # Reassiging head node to new_node
        for i in range(index-1):
            curr_node = curr_node.next
        new_node.next = curr_node.next
        curr_node.next = new_node
        return head
    def display(self,head):
        while True:
            try:
                print(head.data)
                head = head.next
            except AttributeError:
                break
    def creating(self):
        n = int(input("Enter the no of nodes: "))
        arr = list(map(int,input("Enter the list Elements:\n").split()))
        try:
            curr_node = Node(arr[0])
            head = curr_node
        except IndexError:# If n is 0 then assign first_node to None
            head = None
        for i in range(1,n):
            curr_node.next = Node(arr[i])
            curr_node = curr_node.next
        return head
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
linked_list = LinkedList()
head = linked_list.creating()
index = int(input("Enter the index to be inserted: ")) # The index should be between 1<=index<=n
element = int(input("Enter the element to be inserted: "))
head = linked_list.inserting(head,index,element)
linked_list.display(head)