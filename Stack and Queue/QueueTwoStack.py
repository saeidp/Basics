class Queue_using_stack():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def empty(self):
        return len(self.stack1) + len(self.stack2) == 0
    
    def enqueue(self, data):
        self.stack1.append(data)
    
    def dequeue(self):
        if self.empty():
            return Exception("Empty Queue")
        if len(self.stack2) == 0:
            while(len(self.stack1) != 0):
                # val = self.stack1[-1]
                val = self.stack1.pop()
                self.stack2.append(val)
        val = self.stack2.pop()
        return val

q = Queue_using_stack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue(), q.dequeue(), q.dequeue())