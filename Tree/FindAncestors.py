class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

# you have to implement findAncestors() function which will
#  find the ancestor of the node whose value is “k”
# bst = {
#	6 -> 4,9
#   4 -> 2,5
#   9 -> 8,12
#   12 -> 10,14
#}
# k=10 -> 12, 9, 6
def findAncestors(root, k):
    result = []
    recur(root, k, result)
    return str(result)

# Helper Recursive function to find ancestors of a node and add them 
# to the result list
def recur(root, k, result):
    # base case
    if root == None:
        return False
    if root.data == k:
        return True
    # to check if target present in either left or right
    # subtree of currentNode
    if recur(root.left, k, result) or \
       recur(root.right, k, result):
       result.append(root.data)
       return True
    return False


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


print(findAncestors(root, 10)) # [12, 9, 6]




