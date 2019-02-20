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

	#1.Start with Enqueuing 1.
	#2.Dequeue a number from queue and append 0 to it and enqueue it back to queue.
	#3.Perform step 2 but with appending 1 to the origional number and enqueue back to queue.
	#Queue takes integer values so before enqueueing it make sure to convert String to integer.
	#Size of Queue should be 1 more than number because for a single number we're enqueing two
	#variations of it , one with appended 0 while other with 1 being appended.
def findBin(number):
    result = []
    queue = Queue()
    queue.enqueue(1)
    for i in range(number):
      result.append(str(queue.dequeue()))
      s1 = result[i] + "0"
      s2 = result[i] + "1"
      queue.enqueue(int(s1))
      queue.enqueue(int(s2))
      
    return result #For number = 3 , result = {"1","10","11"}
