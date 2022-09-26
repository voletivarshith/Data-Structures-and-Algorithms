class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def creation(self):
        n = int(input("Enter the number of nodes: "))
        arr = list(map(int,input("Enter the elements in an array:\n").split()))
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
        while head!=None:
            print(head.data)
            head = head.next
    def removeDuplicateElements(self,head):
        first_node = head # Assigning the first_node as head
        while True:
            try:
                curr_node = head # Assigning the curr_node
                next_node = head.next # Assigning the next_node
                if curr_node.data == next_node.data:# checking whether the curr_node.data is equal to next_node.data
                    curr_node.next = next_node.next# Changing the address of curr_node.data
                else:
                    head = head.next # if not equal then traversing the head variable
                pass
            except AttributeError:
                return first_node
linked_list = LinkedList()
head = linked_list.creation()
linked_list.display(linked_list.removeDuplicateElements(head))