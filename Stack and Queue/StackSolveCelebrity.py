# solution without stack
def findCelebrity(party, numPeople):
    celebrity = -1
    for i in range(numPeople):
        foundCelebrity = True
        for j in range(numPeople):
            if party[i][j] == 1:
                foundCelebrity = False
                break
        if foundCelebrity:
            celebrity = i
            return celebrity
    return celebrity

party =  [ [0,1,1,0], [1,0,1,1], [0,0,0,0], [0,1,1,0]]
row = findCelebrity(party, 4)
print(row)
#--------------------------------------------------------------------
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

def findCelebrity2(party, numPeople):
    stack = Stack()
    celebrity = -1

    for i in range (numPeople):
        stack.push(i)
    while stack.isEmpty() == False:
        #Take two people out of stack and check if they know each other
     	#One who doesn't know the other, push it back in stack.
        x = stack.pop()
        if stack.isEmpty() == True:
            celebrity = x
            break
        y = stack.pop()
        if party[x][y] == 1:
            # x knows y, discard x and push y in stack
            stack.push(y)
        else:
            stack.push(x)

   #At this point we will have last element of stack as celebrity
   #Check it to make sure it's the right celebrity

    for j in range(numPeople):
        #Celebrity knows no one while everyone knows celebrity
        if celebrity != j and (party[celebrity][j] == 1 or party[j][celebrity] == 0):
            return -1
    
    return celebrity

party =  [ [0,1,1,0], [1,0,1,1], [0,0,0,0], [0,1,1,0]]
row = findCelebrity2(party, 4)
print(row)