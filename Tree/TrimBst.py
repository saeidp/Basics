# Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
   
def printTree(current):
    if current == None:
        return
    print(str(current.data), end=" " ) 
    printTree(current.left)
    printTree(current.right)
 
#-----------------------------------
# Given the root of a binary search tree and 2
# numbers min and max, trim the tree such that all
# the numbers in the new tree are between min 
# and max (inclusive). The resulting tree should still
# be a valid binary search tree. So, if we get this 
# tree as input

# We can do this by performing a post-order traversal of 
# the tree. We first process the left children, then right
# children, and finally the node itself

# The complexity of this algorithm is O(N), where N is the 
# number of nodes in the tree
def trimBST(tree, minVal, maxVal): 
    
    if not tree: 
        return 
    
    tree.left=trimBST(tree.left, minVal, maxVal) 
    tree.right=trimBST(tree.right, minVal, maxVal) 
    
    if minVal<=tree.data<=maxVal: 
        return tree 
    
    if tree.data<minVal: 
        return tree.right 
    
    if tree.data>maxVal: 
        return tree.left

root = Node(8)
root.left = Node(3)
root.right = Node(10)

root.left.left = Node(1)
root.left.right = Node(6)

root.left.right.left = Node(4)
root.left.right.right = Node(7)

root.right.right = Node(14)
root.right.right.left = Node(13)

root = trimBST(root, 5, 13)
printTree(root) # 8, 6, 7, 10, 13

#     8
# 6       10
#   7        13