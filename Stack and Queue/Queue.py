class myQueue:
  
    def __init__(self, s):
        self.size = s
        self.queueArray = []
        self.front = 0
        self.back = -1
        self.numOfItems = 0
    
    def enqueue(self,value):
      if self.isFull() == True:
        print("Queue is Full!")
        return
      if self.back == self.size -1:
        self.back = - 1
      self.back += 1
      self.queueArray.insert(self.back,value)
      self.numOfItems+=1
    
    def dequeue(self):
      if self.isEmpty() == True:
        print("Queue is Empty!")
        return
      temp = self.queueArray[self.front]
      self.front += 1
      if self.front == self.size:
        self.front = 0      
      self.numOfItems -=1
      return temp
    
    def getTop(self):
      if self.isEmpty() == False:
        return self.queueArray[self.front]
      else:
        print("Stack is Empty!")
      
    def isEmpty(self):
      if self.numOfItems == 0:
        return True
      return False
    
    def isFull(self):
      if self.numOfItems == self.size:
        return True
      return False
    
    def getSize(self):
        return self.numOfItems
        
queue = myQueue(5) 

queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(6)
queue.enqueue(8)
queue.enqueue(10)

print("Is queue full()?: " + str(queue.isFull())) 
		
print("Dequeue(): " + str(queue.dequeue()))
print("Dequeue(): " + str(queue.dequeue()))
		
print("getTop(): " + str(queue.getTop())) 

queue.enqueue(12)
queue.enqueue(14)

while queue.isEmpty() == False:
		print("Dequeue(): " + str(queue.dequeue()))
    
print("Is queue empty()?: " + str(queue.isEmpty()))    