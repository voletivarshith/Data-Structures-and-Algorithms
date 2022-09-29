# 141 LinkedList Cycle
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index 
of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

let us initialize an empty set as node list
traverse the head node until the head value become None
check if the head node in the node list then return True then the node is repeated else
add the node in the node list set and traverse the node 
if the head node reached last of the linked list then return False
"""
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def creation(self):
        n = int(input("Enter the number of nodes: "))
        arr = list(map(int,input("Enter the number of elements: \n").split()))
        pos = int(input("Enter the position: "))
        node = None
        try:
            first_node = Node(arr[0])
            head = first_node
            if pos==0:
                node = first_node
                node.next = None
        except IndexError:
            return None
        for i in range(1,n):
            first_node.next = Node(arr[i])
            first_node = first_node.next
            if i-1 == pos:
                print(node.data,node.next)
                node = first_node
        # self.display(node)
        first_node.next = node 
        return head
    def linkedListCycle(self,head):
        node_set = set()
        while head:
            if head in node_set:
                return True
            else:
                node_set.add(head)
            head = head.next
        return False
    def display(self,head):
        count = 0
        while head:
            print(head.data)
            head = head.next
            count = count + 1
            if count==10:
                break

linked_list = LinkedList()
head = linked_list.creation()
print(linked_list.linkedListCycle(head))