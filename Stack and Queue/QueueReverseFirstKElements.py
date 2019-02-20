class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
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

# k=5
# queue: 1 2 3 4 5 6 7 8 9 10
# queueNew: 1 2 3 4 5 10 9 8 7 6
# first means the values entered the first. In this sample the first 5 elements of queue
# 6 7 8 9 10 (10 is thefirst and goes to fith)
def reverseFirstK(queue, k):
    if queue.isEmpty == False:
        return
    if k > queue.size():
        return
    stack= Stack()
    queueReverse = Queue()
    for _ in range(k):
        stack.push(queue.dequeue())
    
    for _ in range(stack.size()):
        queueReverse.enqueue(stack.pop())
    
    for _ in range(queue.size()):
        queueReverse.enqueue(queue.dequeue())
    return queueReverse



queue = Queue()
queue.enqueue(10)
queue.enqueue(9)
queue.enqueue(8)
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(5)
queue.enqueue(4)
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(1)

queueNew = reverseFirstK(queue, 4)
print ("done")
