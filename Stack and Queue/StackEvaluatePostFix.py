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

#you have to implement evaluatePostFix() function which will take
# a mathematical expression as an input and return the result of that expression
def evaluatePostFix(exp):
    stack = Stack()
    
		#1.Scan expression character by character,
		#2.If character is a number push it in stack
		#3.If character is operator then pop two elements from stack
		#perform the operation and put the result back in stack
		#At the end, Stack will contain result of whole expression.
    for i in range(len(exp)):
        character = exp[i]
        if character.isdigit()==False:
            x = stack.pop()
            y = stack.pop()
            if character == '+':
                stack.push(x + y)
            elif character == '-':
                stack.push(x - y)
            elif character == '*':
                stack.push(x * y)
            elif character == '/':
                stack.push(x / y)
        else:
            stack.push(int(character)) 
    return stack.pop()

result = evaluatePostFix("219*-8-4+")
print(result) # 5
