class Queue:

    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
       return self.items.pop()
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
