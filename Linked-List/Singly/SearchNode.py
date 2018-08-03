#Linked List head is Node(-1)
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
    temp=self.headNode.nextElement     
    while(temp.nextElement!=None):
     print( temp.data , "->",end=" ")
     temp=temp.nextElement    
    print(temp.data , "-> None")
    return True    
  
  def insertAtHead(self,data):
    node = Node(data)
    node.nextElement = self.headNode.nextElement
    self.headNode.nextElement = node
    return self.headNode


def searchNode(list, value):
  if(list.isEmpty()):
    return False
  head = list.getHead()
  current = head.nextElement
  while(current !=None):
    if(current.data == value):
      return True
    current = current.nextElement
  return False

list = LinkedList()
list.insertAtHead(4)
list.insertAtHead(10)
list.insertAtHead(90)
list.insertAtHead(5)
print(searchNode(list, 5))