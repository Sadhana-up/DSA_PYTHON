##Insert at the end

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

head = node1 
current = head
new_node = Node(80)
while current.next is not None:
    current = current.next
current.next = new_node

# Print linked list (Optional , It is just like traversing)
current = head
while current is not None:
    print(current.data, end=" → ")
    current = current.next
print("None")







    