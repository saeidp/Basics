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
    node= Node(data)
    node.nextElement = self.headNode.nextElement
    self.headNode.nextElement = node
    return self.headNode

list = LinkedList()
for i in range(1,10,1):
  list.insertAtHead(i)
list.printList()