# A deque, also known as a double-ended queue, is an ordered collection of items similar
# to the queue. It has two ends, a front and a rear, and the items remain positioned in the collection.
# What makes a deque different is the unrestrictive nature of adding and removing items.
# New items can be added at either the front or the rear. Likewise, existing items can be removed from either end.
# In a sense, this hybrid linear structure provides all the capabilities of stacks and queues in a single data structure.

class Dequeue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
       return self.items.pop(0)

d = Dequeue()
d.addFront(1)
d.addRear(2)
print(d.removeFront()) #1

