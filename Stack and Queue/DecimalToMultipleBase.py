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


class DecimalToMultipeBase:
    def convert(self, num, numBase):
        digits = Stack()
        while True:
            digits.push(num % numBase)
            num //= numBase
            if(num== 0):
                break
        while digits.isEmpty() != True:
            print(digits.pop(), end='')

decimalToBase = DecimalToMultipeBase()

decimalToBase.convert(12, 10)  # 1 2

print()

decimalToBase.convert(12, 2)   # 1 1 0 0
