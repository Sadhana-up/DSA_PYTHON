##DELTE MIDDLE ELEMENT FROM A STACK
def delete_middle(stack, current=0):
    size = len(stack)
    middle = size // 2
    
    # Base case: if we are at the middle
    if current == middle:
        stack.pop()
        return
    temp = stack.pop()
    delete_middle(stack, current + 1)
    stack.append(temp)
    
    

# Example
stack = [1, 2, 3, 4, 5]
delete_middle(stack)
print("Stack after deleting middle:", stack)
