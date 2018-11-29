class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
# Finding the nodes at k distance from root. (number of edges to root)
#bst = {
#    6 -> 4,9
#    4 -> 2,5
#    9 -> 8,12
#    12 -> 10,14
# k=2 -> 2, 5, 8, 12

def findKDistantNodes(root, k):
    res = []
    findKDistant(root, k, res)
    return str(res)

def findKDistant(root, k, res):
    if root == None:
        return
    if k == 0:
        res.append(root.data)
    else:
        findKDistant(root.left, k - 1, res)
        findKDistant(root.right, k - 1, res)

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

print(findKDistantNodes(root, 2))