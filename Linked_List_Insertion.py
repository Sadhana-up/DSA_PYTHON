#Insert a new element as a node in linked list

#AT THE BEGINNING 

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

#Create Nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next= node2
node2.next = node3
node3.next = node4

head = node1 #Node is always the head 
new_node = Node(50)
new_node.next = head
head = new_node



    