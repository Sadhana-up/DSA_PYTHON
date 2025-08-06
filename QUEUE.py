q =[]
max_size = 10
def enqueue():
    x = int(input("Insert the element you want to add"))
    add = q.append(x)
    print(f"{add} has been added to your queue")
    print(q)

def dequeue():
    if len(q)==0:
        print("q is empty")
    else:
        q.pop(0)

def peek():
    a=q.pop(-1)
    print(a)

def Is_Full():
    if len(q) == max_size:
        print("Queue is Full")
    else:
        print("Not full")

def display():
    print(q)
while True:
    print('''choose:
          1.Enqueue
          2.Dequeue
          3.Peek
          4.Is_full
          5.Display''')
    
    choice = int(input("Choose one: "))

    if choice ==1:
        enqueue()
    
    elif choice ==2:
        dequeue()
    
    elif choice ==3:
        peek()
    
    elif choice ==4 :
        Is_Full()
    
    else:
        display()

    




    

