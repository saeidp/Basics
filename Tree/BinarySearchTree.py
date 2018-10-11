class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

class binarySearchTree:
    def __init__(self, value):
        self.root = Node(value)
    
    def isEmpty(self):
        return self.root == None

    def printTree(self, current):
        if current == None:
            return
            
        print(str(current.data), end=" " ) 
        self.printTree(current.left)
        self.printTree(current.right)
    
    def add(self, value):
        if self.isEmpty():
            self.root = Node(value)
            return True
        current = self.root
        while current != None:
            left = current.left
            right = current.right
            if current.data > value:
                if left == None:
                    left = Node(value)
                    current.left = left
                    return True
                current = left
            else:
                if right == None:
                    right = Node(value)
                    current.right = right
                    return True
                current = right
        return False
    
    def search(self, value):
        if self.isEmpty():
            return "List is Empty!"
        current = self.root
        while current != None:
            if current.data == value:
                return str(current.data)
            if current.data > value:
                current = current.left
            else:
                current = current.right
        return str(value) + " is not in the tree!"
    
    
    #Pre Order Traversal: root-left-right
    def preTraverse(self, root):
        if root == None:
            return
        print(str(root.data), end=" ")
        self.preTraverse(root.left)
        self.preTraverse(root.right)
    
    #In Order Traversal: left-root-right
    def inTraverse(self, root):
        if root == None:
            return
        self.inTraverse(root.left)
        print(str(root.data), end = " ")
        self.inTraverse(root.right)

    #Post Order Traversal: left-right-root
    def postTraverse(self, root):
        if(root == None):
            return
        self.postTraverse(root.left)
        self.postTraverse(root.right)
        print(str(root.data), end = " ")
        



def mainAdd():
    
        #6
  #4           #9
#2  #5     #8      #12
                #10   #14  
   
    bst = binarySearchTree(6)
    bst.add(4)
    bst.add(9)
    bst.add(5)
    bst.add(2)
    bst.add(8)
    bst.add(12)
    bst.add(10)
    bst.add(14)
    bst.printTree(bst.root)
    print()  #6 4 2 5 9 8 12 10 14

    result = bst.search(19) 
    print(result) #19 is not in the tree!

    bst.preTraverse(bst.root) #6 4 2 5 9 8 12 10 14
    print()

    bst.inTraverse(bst.root) #2 4 5 6 8 9 10 12 14
    print()

    bst.postTraverse(bst.root) #2 5 4 8 10 14 12 9 6
    print()

mainAdd()

