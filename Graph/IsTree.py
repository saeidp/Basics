
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class Node:

    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

# Linked List class contains a Node object
class LinkedList:

    def __init__(self):
        self.head = None

    # Functio to insert a new node at the beginning
    def insertAtHead(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    # This function is in LinkedList class. Inserts a
    # new node after the given prev_node.
    def insertAfter(self, prev_node, new_data):

        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

    # This function is defined in Linked List class
    # Appends a new node at the end.
    def insertAtTail(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

        # Given a reference to the head of a list and a key,
        # delete the first occurence of key in linked list
    def deleteNode(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if(temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []
        for _ in range(vertices):
            temp = LinkedList()
            self.array.append(temp)
    
    def addEdge(self, source, destination):
        self.array[source].insertAtHead(destination)
    
    def printGraph(self):
        print(">>Adjacency List of Directed Graph<<")
        print()
        for i in range(self.vertices):
            print("|", i, "| => ", end="")
            temp = self.array[i].head
            while temp != None:
                print("[" , temp.data, "] -> ", end="")
                temp = temp.next       
            print("None")
#-----------------------------------------------------------
# In this problem, you have to implement isTree() function
# which will take a graph as an input and find out if it is
# a tree. Remember, a Graph could only be true under two
# conditions which are stated below. An illustration is also
# provided for your understanding.
# there are no cycles
# graph is connected
# Being connected means that starting from any vertex we can
# reach all the vertices of the Graph.
# g is an undirected graph
def isTree(g):
    hasCycle = True
    isConnected = False
    start = 0
    #1. Check for Cycle
    hasCycle = detectCycle(g, start)
    #2. Check for connectivity
    isConnected = checkConnected(g, start)
    print("Has cycle? : " + str(hasCycle) + " Is connected? : " + str(isConnected))
    if(not hasCycle and isConnected):
        return True #Is a Tree
    return False #Not a Tree

def detectCycle(g, source):
    num_of_vertices = g.vertices
    visited = []
    for _ in range(num_of_vertices):
        visited.append(False)
    stack = Stack()
    stack.push(source)
    visited[source] = True
    while(stack.isEmpty() == False):
        # current_node is actual the index of the graph array
        current_node = stack.pop()
        temp = g.array[current_node].head
        while(temp != None):
            if(visited[temp.data] == False):
                stack.push(temp.data)
                visited[temp.data] = True
            else:
                return True
            temp = temp.next
    return False

def checkConnected(g,source):
    num_of_vertices = g.vertices
    vertices_reached = 0 #Store vertices reachable through source
    #A list to hold the history of visited nodes (by default all false)
    #Make a node visited whenever you push it into stack
    visited = []
    for _ in range(num_of_vertices):
        visited.append(False)
    #Create Stack(Implemented in previous lesson) for Depth First Traversal and Push source in it
    stack = Stack()
    stack.push(source)
    visited[source] = True
    #Traverse while stack is not empty
    while (not stack.isEmpty()):
        #pop a vertex/node from stack
        current_node = stack.pop()
        #Get adjacent vertices to the current_node from the list,
        #and push unvisited vertices in stack and also increment vertices_reached 
        temp = g.array[current_node].head
        while (temp != None):
            if(not visited[temp.data]):
                stack.push(temp.data)
                visited[temp.data] = True
                vertices_reached+=1
            temp = temp.next
    #+1 for source, and if number of vertices reachable from source are equal
    #to the total number of vertices in graph then return true else false
    return (vertices_reached + 1) == g.vertices 

g = Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(3,4)
g.printGraph()
print("Is Tree? " + str(isTree(g))) # is a tree

g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(3,2)
g.printGraph()
print("Is Tree? " + str(isTree(g))) # is not a tree. it has cycle

