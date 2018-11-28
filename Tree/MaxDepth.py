class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
#-----------------------------------------------
# Find the height (or maximum depth) of a given binary search tree
# Height of a Node — Maximum number of connections
# between the node and a leaf node in its path (edges)
#
# Height of a Node — Number of nodes on longest path
# we follow the second approach number of nodes   
# Recursively calculate height of left and right
# subtrees of a node and assign height to the node as max
# of the heights of two children plus 1

# bst = {
# 6 -> 4,9
# 4 -> 2,5
# 9 -> 8,12
# 12 -> 10,14
#}
# -> height = 4

# Compute the "maxDepth" of a tree -- the number of nodes  
# along the longest path from the root node down to the  
# farthest leaf node 
def maxDepth(node): 
    if node is None:
        return 0
    else :
        # Compute the depth of each subtree 
        lDepth = maxDepth(node.left) 
        rDepth = maxDepth(node.right) 
        # Use the larger one 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1

root = Node(6)
root.left = Node(4)
root.right = Node(9)
root.left.left = Node(2)
root.left.right = Node(5)

root.right = Node(9)
root.right.left = Node(8)
root.right.right = Node(12)

root.right.right.left = Node(10)
root.right.right.right = Node(14)

height = maxDepth(root)
print(height)

