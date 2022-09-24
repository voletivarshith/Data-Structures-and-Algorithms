# Inserting an element in a sorted linkedlist
"""
There are 3 cases in inserting an element
Case 1 At beginning
Case 2 At middle 
Case 3 At end
"""
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def creation(self):
        n = int(input("Enter the number of nodes: "))
        arr = list(map(int,input("Enter the elements in an array: \n").split()))
        try:
            head = Node(arr[0])
            curr_node = head
        except IndexError:
            return None
        for i in range(1,n):
            curr_node.next = Node(arr[i])
            curr_node = curr_node.next
        return head
    def insertingInAnOrder(self,head,ele):
        first_node =head
        try:
            node_to_be_inserted = Node(ele)
            min = head.data # Minimum
            if min>=ele:# Case 1
                node_to_be_inserted.next = head
                return node_to_be_inserted
        except:
            return node_to_be_inserted #If the linked list has no elements
        while True:
            try:
                # min = head.data # Min is the current element
                max = head.next.data #max is the next element 
                if(max>=ele): # check if the element is between minimum and maximum then
                    temp_node = head.next # temp_node is assigning the head next address
                    head.next = node_to_be_inserted # changing the head next node to new node 
                    node_to_be_inserted.next = temp_node # assigning the new_node next value to the next node
                    return first_node
                head = head.next
            except AttributeError:
                break
        head.next = node_to_be_inserted
        return first_node
    def display(self,head):
        while True:
            try:
                print(head.data)
                head = head.next
            except AttributeError:
                break
linked_list = LinkedList()
head = linked_list.creation()
ele = int(input("Enter an element in a sorted order: "))
linked_list.display(linked_list.insertingInAnOrder(head,ele))