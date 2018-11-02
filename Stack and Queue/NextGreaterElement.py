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

# it is a solution but doesn't use the stack that much
#[4,6,3,2,8,1] - > [6,8,8,8,-1,-1]: It assign the next grater value 
# and if not found or the last array item insert -1
def nextGreaterElement(arr):
    stack = Stack()
    result = []
    for i in range(len(arr)):
        greater = -1
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                greater = arr[j]
                break
        stack.push(greater)
    
    while stack.isEmpty() == False:
        result.insert(0, stack.pop())

    return result

arr =[4,6,3,2,8,1]
result = nextGreaterElement(arr)
print(result) # -> [6,8,8,8,-1,-1]       
