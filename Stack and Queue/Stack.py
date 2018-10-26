class myStack:

    #Stack Constructor
    def __init__(self, s):
        self.size = s
        self.stackArray = []
        self.top = -1 
        
    #Returns top element    
    def getTop(self):
      if self.isEmpty() == False:
        return self.stackArray[self.top]
      else:
        return "Stack is Empty!"
        
    #Returns True if Stack is empty  
    def isEmpty(self):
      if self.top == -1:
        return True
      return False
    
    #Returns True if Stack is full
    def isFull(self):
      if self.top == self.size - 1:
        return True
      return False    
        
    #Inserts the element at top
    def push(self,value):
      if self.isFull() == True:
        return "Stack is Full!"
      self.top +=1
      self.stackArray.insert(self.top,value)
        
    #Removes and returns the element at top
    def pop(self):
      if self.isEmpty() == False:
        temp = self.stackArray[self.top]
        self.top -= 1
        return temp
      return "Stack is Empty!"

stack = myStack(5)

for i in range(5):
  stack.push(i)  

print("Is stack full()?: " + str(stack.isFull()))
print("getTop(): " + str(stack.getTop()))
  
for x in range(5):
  print(stack.pop())

print( "Is stack empty()?: " + str(stack.isEmpty()))