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
  
    #Helper function to find least value node in right-subtree of currentNode
    def findLeastNode(self,currentNode):
        temp = currentNode
        while (temp.left != None):
            temp = temp.left
        return temp
    
    
    # 1. Deletion at Leaf Node : we simply remove that leaf node.
    # After deletion, its parent node will point to None
    # 2. Deletion at Parent Node: can further be sub-divided into
    # two cases:
    # Parent Node has only one child
    # Parent Node has two children
    #2.1 Parent Node has only one Child: Link the parent node
    # with the 1st child of current node (to be deleted)
    #2.2 Parent Node has Two Children: Follow the steps below:
    #2.2.1: From the parent node to be deleted, traverse its 
    # right subtree in a such a way that you reach the l
    # eft-most value. That value will appear to be the smallest
    # value in the whole subtree
    #2.2.2: Replace the node’s value with parent’s node value
    #2.2.3: Finally, delete the leaf node
    
    # Conditions for Deletion
    #1.node is leaf node
    #2.node has 1 child
    #3.node has 2 children
    def delete(self, value, start):
        currentNode = start
        parent = None
        isLeftChild = False
        while currentNode != None:
            #Node to be deleted found
            if currentNode.data == value:
                left = currentNode.left
                right = currentNode.right

                #1. Node is leaf Node
                if left == None and right == None:
                    if isLeftChild:
                        parent.left = None
                    else:
                        parent.right = None
                    return True
                #3. Node has 2 Children
                elif left !=None and right != None:
                    #Find Least Value Node in right-subtree of current Node
                    leastNode = self.findLeastNode(right)
                    #Set CurrentNode's Data to the least value in its right-subtree
                    currentNode.data = leastNode.data
                    #Delete the leafNode which had the least value
                    # we send the right node because we want the
                    # isLeftChild to be assigned a value
                    self.delete(leastNode.data, right)
                    return True
                #2. Node has 1 Child
                else:
                    #Node has a LeftChild
                    if left != None:
                        if isLeftChild:
                            parent.left = left
                        else:
                            parent.right = left
                    #Node has a RightChild
                    else:
                        if isLeftChild:
                            parent.left = right
                        else:
                            parent.right = right
                        return True
            #end of if currentNode.data == value
            elif currentNode.data > value:
                isLeftChild = True
                parent = currentNode
                currentNode = currentNode.left
            else:
                isLeftChild = False
                parent = currentNode
                currentNode = currentNode.right
        #End of While
        print(str(value) + " is not in tree!")
        return False


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

    bst.printTree(bst.root)
    print("\nDeleting Leaf Node 2 : ")
    bst.delete(2, bst.root)
    bst.printTree(bst.root)
    print("\nDeleting Node 9 having 2 Children : ")
    bst.delete(9, bst.root)
    bst.printTree(bst.root)
    print("\nDeleting Node 12 having 1 Child : ")
    bst.delete(12, bst.root)
    bst.printTree(bst.root)

mainAdd()

