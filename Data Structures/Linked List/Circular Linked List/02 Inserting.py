class Node:
    def __init__(self,data,next=None):
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
        first_node.next = head
        return head
    def insertion(self,first_node,pos,ele):
        flag = 0
        if pos==1:
            temp = Node(ele)
            temp.next = first_node
            head = temp
            while temp.next!=first_node or flag == 0:
                flag = 1
                temp = temp.next
            temp.next = head
        return head
    def display(self,head):
        temp = head
        while head.next!=temp:
            print(head.data)
            head = head.next
        print(head.data)
linked_list = LinkedList()
head = linked_list.creation()
pos = int(input("Enter the position to be inserted: "))
ele = int(input("Enter the value to be inserted in a linked list: "))
head = linked_list.insertion(head,pos,ele)
linked_list.display(head)