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

# Simple Balanced Parentheses
def parCheckerSimple(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while(index < len(symbolString) and balanced):
        symbol = symbolString[index]
        if(symbol == "("):
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index +=1
    if(balanced and s.isEmpty()):
        return True
    else:
        return False

print(parCheckerSimple("(())"))

# Complex Blanced Parantheses
def parCheckerComplex(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(parCheckerComplex('{{([][])}()}'))
print(parCheckerComplex('[{()]'))