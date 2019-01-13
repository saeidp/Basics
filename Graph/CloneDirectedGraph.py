# Clone a Directed Graph
# Given root node of a directed graph, clone this graph by creating its deep copy
# such that cloned graph has same vertices and edges as the original graph.
# Hints
# Use hash table
# Depth first traversal

#Runtime Complexity
#Linear, O(n).Memory Complexity Logarithmic, O(n). 'n' is number of vertices
# in graph.

# We use depth first traversal and create a copy of each node while traversing
# the graph. To avoid getting stuck in cycles, we'll use a hashtable to store
# each completed node and will not revisit nodes that exist in the hashtable.
# Hashtable key will be a node in the original graph, and its value will be the
# corresponding node in cloned graph.
# For above graph lets assume root is node '0'. We'll start with the root
# node i.e. '0'.
class Node:
    def __init__(self, d):
        self.data = d
        self.neighbors = []

def clone_rect(root, nodes_completed):
    if root == None:
        return None

    pNew = Node(root.data)
    nodes_completed[root] = pNew

    for p in root.neighbors:
        x=nodes_completed.get(p)
        if (x==None):
            pNew.neighbors += [clone_rect(p, nodes_completed)]
        else:
            pNew.neighbors +=[x]
    return pNew

def clone(root):
    nodes_completed = {}
    return clone_rect(root, nodes_completed)

p0 = Node(0)
p1 = Node(1)
p2 = Node(2)
p3 = Node(3)
p4 = Node(4)

p0.neighbors = [p2,p3,p4]
p2.neighbors = [p0]
p1.neighbors = [p2]
p3.neighbors = [p2]
p4.neighbors = [p0, p1, p3]

pNew = clone(p0)
