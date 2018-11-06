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

def isBalanced(exp):
    if len(exp) % 2 != 0:
        return False
    opening = set("([{")
    matches = set([ ("(",")"), ("[", "]"), ("{", "}") ])
    stack= Stack()
    for paren in exp:
        if paren in opening:
            stack.push(paren)
        else:
            if stack.size() == 0:
                return False
            lastOpen = stack.pop()
            if (lastOpen, paren) not in matches:
                return False
    return stack.size() == 0


print(isBalanced('[](){([[[]]])}')) # True

#----------------------------------------------------------------------------------
#second approach
def isBalanced2(exp):
  #Iterate through the string exp.
	#For each opening parentheses, push it into stack
	#For every closing parentheses check for its opening parentheses in stack
	#If you can't find the opening parentheses for any closing one then returns false.
	#and after complete traversal of string exp, if there's any opening parentheses left
	#in stack then also return false.
	#At the end return true if you haven't encountered any of the above false conditions.
  stack = Stack()
  
  for i in range(len(exp)):
    character = exp[i]
    if (character == '}' or character == ')' or character == ']'):
      if (stack.isEmpty()):
      	return False
			
      if ((character == '}' and stack.pop() != '{') or (character == ')' and stack.pop() != '(') or (character == ']' and stack.pop() != '[')):
        return False
    else: 
    	stack.push(character)
  if (stack.isEmpty() == False):
    return False
  return True
    
print(isBalanced2('[](){([[[]]])}')) # True