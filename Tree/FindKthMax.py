class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
#-----------------------------------------------

# you have to implement findKthMax() function which 
# will take a BST and any number “k” as an input and
# return kth maximum number from that tree
# bst = {
#	6 -> 4,9
#   4 -> 2,5
#   9 -> 8,12
#   12 -> 10,14
#}
# k=3 => 10
def findKthMax(root, k):
    tree = []
    inTraverse(root, tree)
    if len(tree) - k >= 0:
        return tree[len(tree) - k]

def inTraverse(root,tree):
    if root.left != None:
        inTraverse(root.left, tree)
    
    tree.append(root.data)
    
    if root.right != None:
        inTraverse(root.right, tree)


root = Node(6)
node4 = Node(4)
node9 = Node(9)
node2 = Node(2)
node5 = Node(5)
node9 = Node(9)
node8 = Node(8)
node12 = Node(12)
node10 = Node(10)
node14 = Node(14)

root.left = node4
root.right = node9

node4.left = node2
node4.right = node5

node9.left = node8
node9.right = node12

node12.left = node10
node12.right = node14

print(findKthMax(root, 3))