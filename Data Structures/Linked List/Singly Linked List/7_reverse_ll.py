# Reversing a linkedlist
"""
This can be done in 2 ways the
1st Way is Reversing the address
2nd way is removing the second node and placing at first(check leetcode problems 0206 reverse a linked list)
Approch 
declare 3 pointers
first node is pointing to first node
second node is pointing to none
third node is pointing to none
assigning the third node to second node
assigning the second node to first node
first node is traversing to the next of first node
second_node.next is assigned to third node
head 1->2->3->4->None
None<-1 2->3->4->None
None<-1<-2 3->4->None
None<-1<-2<-3 4->None
None<-1<-2<-3<-4
"""
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def creation(self):
        n = int(input("Enter the number of nodes: "))
        arr = list(map(int,input("Enter the elements in an array:\n").split()))
        try:
            first_node = Node(arr[0])
            head = first_node
        except IndexError:
            return None
        for i in range(1,n):
            first_node.next = Node(arr[i])
            first_node = first_node.next
        return head
    def display(self,head):
        while head:
            print(head.data)
            head = head.next
    def reverseLinkedList(self,head):
        first_node = head
        second_node = None
        third_node = None
        while first_node:
            third_node = second_node
            second_node = first_node
            first_node = first_node.next
            second_node.next = third_node
        return second_node
linked_list = LinkedList()
head = linked_list.creation()
linked_list.display(linked_list.reverseLinkedList(head))