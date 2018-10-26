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



def reverse2(list):
    if(list.isEmpty()):
        return LinkedList()
    list2 = LinkedList()
    current = list.getHead().nextElement
    while(current != None):
        list2.insertAtHead(current.data)
        current = current.nextElement
    return list2

# list = LinkedList()
# list.insertAtHead(6)
# list.insertAtHead(4)
# list.insertAtHead(9)
# list.insertAtHead(10)
# list.printList()

# list2 = reverse2(list)
# list2.printList()
#---------------------------------------------------------

def reverse(list):
  prev = None #To keep track of the previous element, will be used in swapping links
  current = list.getHead().nextElement #firstElement
  next = None
  
  #While Traversing the list, swap links
  while (current != None):
    next = current.nextElement
    current.nextElement = prev
    prev = current
    current = next
	
  #Linking Head Node with the new First Element
  list.headNode.nextElement = prev

list = LinkedList()
list.insertAtHead(6)
list.insertAtHead(4)
list.insertAtHead(9)
list.insertAtHead(10)
list.printList()

reverse(list)
list.printList()