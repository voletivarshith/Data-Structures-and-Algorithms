class LinkedList:
    def display(self,head):#Displaying the elements in linkedlist
        while True:
            try:
                print(head.data)
                head = head.next
            except AttributeError:
                break
    def creating(self):
        n = int(input("Enter no of nodes: "))
        arr = list(map(int,input("Enter the elements:\n").split()))
        try:
            curr_node = Node(arr[0])
            head = curr_node
        except IndexError:# If n is 0 then assign head to None
            head = None
        for i in range(1,n):
            curr_node.next = Node(arr[i])
            curr_node = curr_node.next
        return head
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
linked_list = LinkedList()
head = linked_list.creating()
linked_list.display(head)