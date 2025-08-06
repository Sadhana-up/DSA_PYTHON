arr = []

def push():
    num = int(input("Enter number to push: "))
    arr.append(num)
    print(f"{num} has been added to the array")

def pop_element():
    if len(arr) == 0:
        print("Stack is empty. Nothing to pop.")
    else:
        x = arr.pop()
        print(f"{x} has been removed from the array")

def display():
    if len(arr) == 0:
        print("Stack is empty.")
    else:
        print("Stack contents:")
        for i in range(len(arr)):
            print(arr[i])

def is_empty():
    if len(arr) == 0:
        print("Empty stack")
    else:
        print("Stack is not empty")

# Sample menu to test
while True:
    print("\nMenu: 1.Push 2.Pop 3.Display 4.IsEmpty 5.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        display()
    elif choice == 4:
        is_empty()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
