# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
 
 
# create root
root = Node(1)
r''' following is the tree after above statement
        1
      /   \
'''
 
root.left      = Node(2)
root.right     = Node(3)
   
r''' 2 and 3 become left and right children of 1
           1
         /   \
        2      3
     /    \    /  \
'''