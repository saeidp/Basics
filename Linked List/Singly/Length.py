# Linked List head is Node(-1)
class Node:
    def __init__(self, data):
        self.data = data
        self.nextElement = None

class LinkedList:
    def __init__(self):
        self.headNode = Node(-1)

    def isEmpty(self):
        if(self.headNode.nextElement == None):
            return True
        else:
            return False

    def getHead(self):
        return self.headNode

    def printList(self):
        if(self.isEmpty()):
            print("List is Empty")
            return False
        temp = self.headNode.nextElement
        while(temp.nextElement != None):
            print(temp.data, "->", end=" ")
            temp = temp.nextElement
        print(temp.data, "-> None")
        return True

    def insertAtHead(self, data):
        node = Node(data)
        node.nextElement = self.headNode.nextElement
        self.headNode.nextElement = node
        return self.headNode

#------------------------------------------------------
# Access HeadNode => list.getHead()
# Check if list is empty => list.isEmpty();
# Node class  { int data ; Node nextElement;}
def length(list):
    """
    Find Length of Linked List 
    """
    if(list.isEmpty()):
        return 0
    current = list.getHead()
    length = 0
    while(current.nextElement != None):
        length += 1
        current = current.nextElement

    return length


list = LinkedList()
for i in range(1, 10, 1):
    list.insertAtHead(i)
list.printList()

listLength = length(list)
print(listLength)
