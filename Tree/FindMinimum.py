class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
#-------------------------
#  a code to find the minimum value in that tree? 
# NodeValues(LeftSubtree)<=CurrentNodeValue<NodeValues(RightSubTree)
# t = {
# 6-> 4, 9
# 4-> 2,5
# 9->8,12
# 12-> 10, 14}
def findMin(root):
    if root == None:
        return -1
    min = root.data
    current = root.left
    while current != None:
        min = current.data
        current = current.left 
    return min

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
min = findMin(root)
print(min)


