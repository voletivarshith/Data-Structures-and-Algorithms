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
            return head
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
        pos = int(input("Enter the position at which the node to be inserted: "))
        ele = int(input("Enter the element to be inserted: "))
        new_node = Node(ele)
        if pos==0:
            new_node.next = head
            head.prev = new_node
            head = new_node
        else:
            curr_node = head
            for i in range(pos-1):
                # prev_node = curr_node
                curr_node = curr_node.next
            if curr_node.next==None:
                new_node.next = None
                curr_node.next = new_node
                new_node.prev = curr_node
            else:
                new_node.next = curr_node.next
                curr_node.next = new_node
                new_node.prev = curr_node
                temp = new_node
                new_node = new_node.next
                new_node.prev = temp
        curr_node = head
        while head.next!=None:
            head = head.next
        return (curr_node,head)
linked_list = LinkedList()
head,tail = linked_list.creation()
head,tail = linked_list.insertion(head)
linked_list.displayUsingHead(head)
print()
linked_list.displayUsingTail(tail)