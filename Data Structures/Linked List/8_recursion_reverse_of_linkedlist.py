class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
class LinkedList:
    def creation(self):
        n = int(input("Enter the number of nodes: "))
        arr = list(map(int,input("Enter the elements:\n").split()))
        try:
            first_node = Node(arr[0])
            head = first_node
        except IndexError:
            return None
        for i in range(1,n):
            first_node.next = Node(arr[i])
            first_node = first_node.next
        return head
    def recursion(self,head,next_node):
        if head == None:
            return head
        self.recursion(head.next,head)
        head.next = next_node
        print(next_node.data)
    def display(self,head):
        while head:
            print(head.data)
            head = head.next
linked_list = LinkedList()
head = linked_list.creation()
linked_list.recursion(head,head.next)