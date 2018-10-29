#Implement Two Stacks using one Array

#You can either divide list in two halves or start stacks at extreme ends.
#We'll use the second technique to solve this problem. 
#Top of Stack 1 start from extreme left of array i.e top1 = 0;
#Top of Stack 2 start from extreme right of array i.e top2 = size - 1;
class TwoStacks:
    def __init__(self,n):
        self.size = n
        self.arr = []
        self.top1 = -1
        self.top2 = self.size

    def push1(self, value):
        #Check for empty space and insert value if there's an empty space.
        if self.top1 < self.top2 -1:
            self.top1 +=1
            self.arr.insert(self.top1, value)
        return
    
    def push2(self, value):
        #Check for empty space and insert value if there's an empty space.
        if self.top1 < self.top2 -1:
            self.top2 -=1
            self.arr.insert(self.top2, value)
        return
    
    def pop1(self):
        if self.top1 >= 0:
            val = self.arr[self.top1]
            self.top1 -=1
            return val
        return -1
    
    def pop2(self):
        if self.top2 < self.size:
            val = self.arr[self.top2]
            self.top2 +=1
            return val
        return -1


    

#stack-> [1 2 4 3]
stack = TwoStacks(4)
stack.push1(1)
stack.push1(2)
stack.push2(3)
stack.push2(4)


print(stack.pop1(),end =" ")
print(stack.pop2(),end =" ")
print(stack.pop1(),end =" ")
print(stack.pop2(),end =" ")

# 2 4 1 3