class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
#--------------------------------------------------
# O(h). The recursive solution has O(h) memory complexity as
# it will consume memory on the stack up to the height of
# binary tree h. It will be O(log n) for a balanced tree
# and in the worst case can be O(n).

# Two trees 'A' and 'B' are identical if:
# data on their roots is same or both roots are null
# left sub-tree of 'A' is identical to the left sub-tree of 'B'
# right sub-tree of 'A' is identical to the right sub-tree of 'B'
# Driver program to test the above functions

# Let us create the following BST
#      50
#    /      \
#   30     70
#   / \    / \
#  20 40  60 80
def are_identical(root1, root2):
    if(root1 == None and root2 == None):
        return True
    
    if(root1 != None and root2 != None):
        return (root1.data == root2.data and 
                are_identical(root1.left, root2.left) and
                 are_identical(root1.right, root2.right))
    return False

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)

root.right.left = Node(60)
root.right.right = Node(80)

print(are_identical(root, root)) #True
