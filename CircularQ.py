##This is how circular queue works :
#We know  QUEUE has front and rear end 

#INSERTION -> ENQUEUE IS :

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue: insert an element
    def enqueue(self, value):
        # Queue is full if rears next value is the front 
        if (self.rear + 1) % self.size == self.front: ##NO ENQUEUE HERE FOR OBVIOUS REASONS
            print("Queue is full")
            return

        # If queue is empty or is not full then insertion or enqueue can be done
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
        print(f"Enqueued: {value}")

    # Dequeue: remove an element
    def dequeue(self):
        # Queue is empty
        if self.front == -1:
            print("Queue is empty")
            return

        removed = self.queue[self.front]

        # Only one element left
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"Dequeued: {removed}")


# Example usage
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.dequeue()
cq.enqueue(40)

