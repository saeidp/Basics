class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
#-------------------------------------
# Serialize binary tree to a file and then deserialize back
# to tree such that original and deserialized trees are
# identical. Runtime O(n). memory o(Logn)

# One approach is to perform a depth-first traversal 
# and serialize individual nodes to the stream. We'll use
# pre-order traversal here. We'll also serialize some marker
# to represent a null pointer to help deserialize the tree. 
# Consider the below binary tree as an example. 
# Markers (M*) have been added in this tree to represent
# null nodes

# When deserializing the tree we'll again use the pre-order
# traversal and create a new node for every non-marker node.
# Encountering a marker indicates that it was a null node.
import sys
import pickle
MARKER = sys.maxsize
def serialize(node, stream):
  if node == None:
    pickle.dump(MARKER, stream)
    #stream.dump(MARKER)
    return
  pickle.dump(node.data, stream)

  #stream.dump(node.data)
  serialize(node.left, stream)
  serialize(node.right, stream)

def deserialize(stream):
    try:
      data = pickle.load(stream)

      if data == MARKER:
        return None

      node = Node(data)
      node.left = deserialize(stream)
      node.right = deserialize(stream)
      return node
    except pickle.UnpicklingError:
      return None


#        1
#   2        3
# M1  M2   M3  M4 

# Serialize
# 1 2 M1, M2 3 M3 M4
root = Node(1)
root.left = Node(2)
root.right = Node(3)
stream = open('data.pkl', 'wb')
serialize(root,stream)
stream.close()

stream = open('data.pkl', 'rb')
node = deserialize(stream)
stream.close()