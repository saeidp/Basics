#------------------------------------------------------------------------
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

class newStack:
    #Constructor
    def __init__(self):
        #We will use two stacks mainStack to hold origional values
        #and minStack to hold minimum values. Top of minStack will always
        #be the minimum value from mainStack
        self.mainStack = Stack()
        self.minStack = Stack()
    
    #Removes and return value from newStack
    def pop(self):
        #1. Pop element from minStack to make it sync with mainStack,
        #2. Pop element from mainStack and return that value
        self.minStack.pop()
        return self.mainStack.pop()

    #Pushes values into newStack
    def push(self,value):
        #1. Push value in mainStack and check value with the top value of minStack
        #2. If value is greater than top, then push top in minStack
        #else push value in minStack
        self.mainStack.push(value)
        if(self.minStack.isEmpty() == False and value > self.minStack.peek()):
            self.minStack.push(self.minStack.peek())
        else: 
            self.minStack.push(value)
        return True
    #Returns minimum value from newStack in O(1) Time
    def min(self):
        return self.minStack.peek()

s = newStack()
s.push(3)
s.push(5)
s.push(2)
s.push(1)
print (s.min())
#---------------------------------------------------------------------------------------------

# This the first approcha and is explained in geeksforgeeks 
#https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/

# A user defined stack that supports getMin() in 
# addition to push() and pop() 
class MyStack:
    def __init__(self):
        self.items = []
        self.minEle = -1

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.isEmpty():
            self.items.append(item)
            self.minEle = item
        else:
            if item >= self.minEle:
                self.items.append(item)
            else:
                self.items.append(2 * item - self.minEle)
                self.minEle = item

    def pop(self):
        item = self.items.pop()
        if item < self.minEle:
            self.minEle = 2 * self.minEle - item

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
    
    def min(self):
        if self.isEmpty() == False:
            return self.minEle
       

s = MyStack()
s.push(3)
s.push(5)
s.push(2)
s.push(1)
print (s.min())


