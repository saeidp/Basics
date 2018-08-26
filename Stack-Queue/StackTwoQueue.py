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

class Stack_using_queue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    def isEmpty(self):
        return self.queue1.size() + self.queue2.size() == 0
    
    def push(self, data):
        self.queue1.enqueue(data)

    def pop(self):
        if self.isEmpty():
            return Exception("stack is empty")
        while(self.queue1.size() > 1):
            self.queue2.enqueue(self.queue1.dequeue())
        value = self.queue1.dequeue()
        self.swap_queue()
        return value
    
    def swap_queue(self):
        self.queue1, self.queue2 = self.queue2, self.queue1


obj = Stack_using_queue()
obj.push(1)
obj.push(2)
obj.push(3)

print(obj.pop())
print(obj.pop())
print(obj.pop())


