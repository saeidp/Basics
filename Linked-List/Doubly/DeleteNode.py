class Node:
    def __init__(self, data):
        self.data = data
        self.nextElement = None
        self.previousElement = None


class DoublyLinkedList:
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
        next = self.headNode.nextElement
        node.nextElement = next
        if(next !=None):
            next.previousElement = node
        self.headNode.nextElement = node
        node.previousElement = self.headNode
        

        return self.headNode

    def deleteAtHead(self):
        if(self.isEmpty()):
            print("List is Empty")
            return False
        head = self.getHead()
        current = head.nextElement
        head.nextElement = current.nextElement
        current.nextElement.previousElement = head
        print(str(current.data) + " Deleted !")
        return True

  
    def delete(self,value):
        deleted = False
        if(self.isEmpty()):
            print("List is Empty")
            return deleted
        if(self.headNode.nextElement.data == value):
            self.deleteAtHead()
        currentNode = self.headNode.nextElement
        while(currentNode != None):
            if (value == currentNode.data):
                currentNode.previousElement.nextElement = currentNode.nextElement
                deleted = True
                break
            currentNode = currentNode.nextElement
        if (deleted == False):
            print(str(value) + " is not in the List!")
        else:
            print(str(value) + " Deleted!")
        return deleted


list = DoublyLinkedList()
for i in range(1, 5, 1):
    list.insertAtHead(i)

list.printList()
list.delete(1)
list.printList()