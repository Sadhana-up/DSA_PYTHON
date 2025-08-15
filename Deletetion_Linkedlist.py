##Delete the 1st node from a singly linked list 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(10)
node2 = Node(20)
node3 = Node(40)
node4 = Node(50)

head.next = node2
node2.next= node3
node3.next=node4

if head is not None:

    head = head.next

current = head 
while current is not None:
    print(current.data, end="->")
    current = current.next

print("None")
