#Implementing a Queue 

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        return self.queue

# Test the queue
if __name__ == "__main__":
    q = Queue()
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    print(f"Queue after enqueue: {q.display()}")
    print(f"Front element: {q.front()}")
    print(f"Dequeued element: {q.dequeue()}")
    print(f"Queue after dequeue: {q.display()}")