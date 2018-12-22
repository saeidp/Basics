class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
#--------------------------------------------------
# Given a binary tree, figure out whether it's a BST
#A binary search tree holds the property that each node's
# key value is smaller than the key value of all nodes
# in the right subtree and greater than the key values of
# all nodes in the left subtree i.e. L < N < R.

# Solution 1 O(n) using inorder traverse to order the data then 
# check if this order is valid
def is_bst2(root):
    result = []
    result = inOrder(root, result)
    for i in range(len(result) - 1):
        if result[i] >= result[i+1]:
            return False
    return True

def inOrder(root, list):
    if root == None:
        return None
    else:
        if root.left != None:
            inOrder(root.left, list)
        list.append(root.data)
        if root.right !=None:
            inOrder(root.right, list)
        return list

root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(25)
root.left.right = Node(75)
root.right.left = Node(125)
root.right.right = Node(350)
print(is_bst2(root)) #True

root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(25)
root.left.right = Node(125)
root.right.left = Node(150)
root.right.right = Node(350)
print(is_bst2(root)) #False  50 < 125 < 100

#Solution 2 O(n) runtime and o(h) memory (h: is log(n) in balanced tree and n in unbalance)
import sys
def is_bst_rec(root, min_value, max_value):
    if root == None:
        return True
    if root.data < min_value or root.data > max_value:
        return False
    return is_bst_rec(root.left, min_value, root.data) and \
           is_bst_rec(root.right, root.data, max_value) 

def is_bst(root):
    return is_bst_rec(root, -sys.maxsize - 1, sys.maxsize)

root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(25)
root.left.right = Node(75)
root.right.left = Node(125)
root.right.right = Node(350)
print(is_bst(root)) #True

root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(25)
root.left.right = Node(125)
root.right.left = Node(150)
root.right.right = Node(350)
print(is_bst(root)) #False  50 < 125 < 100


# Solution 3 - Another basic approach less efficient than the above
# A basic algorithm would be to check on each node that
#  maximum value of its left sub-tree is less than node's
# data and minimum value of its right sub-tree is greater
#  than node's data
def tree_max(node):
    if not node:
        return float("-inf")
    maxleft  = tree_max(node.left)
    maxright = tree_max(node.right)
    return max(node.data, maxleft, maxright)

def tree_min(node):
    if not node:
        return float("inf")
    minleft  = tree_min(node.left)
    minright = tree_min(node.right)
    return min(node.data, minleft, minright)

def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.data <= tree_min(node.right) and
        verify(node.left) and verify(node.right)):
        return True
    else:
        return False

root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(25)
root.left.right = Node(75)
root.right.left = Node(125)
root.right.right = Node(350)
print(verify(root)) #True

root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(25)
root.left.right = Node(125)
root.right.left = Node(150)
root.right.right = Node(350)
print(is_bst(root)) #False  50 < 125 < 100