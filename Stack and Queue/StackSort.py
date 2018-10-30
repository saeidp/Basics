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

# Simpler implementation using sort method
def sortStack(stack):
    list = []
    for _ in range(stack.size()):
        list.append(stack.pop())
    list.sort( reverse = True)
    for item in list:
        stack.push(item)
    
#1. Use a second tempStack.
#2. Pop value from mainStack.
#3. If the value is greater or equal to the top of tempStack, then push the value in tempStack
#else pop all values from tempStack and push them in mainStack and in the end push value in tempStack and repeat from step 2.
#till mainStack is not empty.
#4. When mainStack will be empty, tempStack will have sorted values in descending order.
#5. Now transfer values from tempStack to mainStack to make values sorted in ascending order.
def sortStack2(stack):
    tempStack = Stack()
    while stack.isEmpty() == False:
        value = stack.pop()
        if tempStack.size() == 0 or value >= tempStack.peek():
            tempStack.push(value)
        else:
            while tempStack.isEmpty() == False:
                stack.push(tempStack.pop())
            tempStack.push(value)
    
    #Transfer from tempStack => stack
    while tempStack.isEmpty() == False:
        stack.push(tempStack.pop())



s = Stack()
s.push(2)
s.push(1)
s.push(4)

sortStack2(s)

for i in range(s.size()):
    print(s.pop(),end=" ") # 1 2 4
