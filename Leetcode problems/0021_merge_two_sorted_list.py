class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def creation(self,arr):
        n = int(input("Enter the number of nodes in first list: "))
        arr = list(map(int,input("Enter the elements:\n").split()))
        try:
            first_node = Node(arr[0])
            head = first_node
        except IndexError:
            return head
        for i in range(1,n):
            first_node.next = Node(arr[i])
            first_node = first_node.next
        return head
    def merge2SortedList(self,list1,list2):
        if list1==None:
            return list2
        if list2==None:
            return list1
        head = None
        if list1.data<=list2.data:
            head = Node(list1.data)
            list1 = list1.next
        else:
            head = Node(list2.data)
            list2 = list2.next
        first_node = head
        while list1 and list2:
            val1 = list1.data
            val2 = list2.data
            if val1<=val2:
                first_node.next = Node(val1)
                list1 = list1.next
            else:
                first_node.next = Node(val2)
                list2 = list2.next
            first_node = first_node.next
        while list1:
            first_node.next = Node(list1.data)
            list1 = list1.next
            first_node = first_node.next
        while list2:
            first_node.next = Node(list2.data)
            list2 = list2.next
            first_node = first_node.next
        return head
    def display(self,head):
        while head:
            print(head.data)
            head = head.next
linked_list = LinkedList()
list1 = linked_list.creation()
list2 = linked_list.creation()
head = linked_list.merge2SortedList(list1,list2)
linked_list.display(head)