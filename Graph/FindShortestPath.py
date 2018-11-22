class Queue:

    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
       return self.items.pop()
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

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
#------------------------------------------------------------
# Find the Shortest Path between Two Vertices
# The path having a minimum number of edges
# will be the shortest path.
# the shortest path will contain the minimum number of edges.
# graph = {
#	0 - 1
#   0 - 2
#   0 - 3
#   3 - 5
#   5 - 4
#   2 - 4
#}
# source = 0, target = 4 then minimum is 2 
# 0=>2=>4 is the minimum edges
def findMin(g, source, destination):
    num_of_vertices = g.vertices
    #A list to hold the history of visited nodes (by default all false)
    #Make a node visited whenever you enqueue it into queue
    visited = [False] * num_of_vertices
    #For keeping track of distance of current_node from source
    distance = [0] * num_of_vertices
    #Create Queue for Breadth First Traversal and enqueue source in it
    queue = Queue()
    queue.enqueue(source)
    visited[source] = True
    #Traverse while queue is not empty
    while (not queue.isEmpty()):
        #Dequeue a vertex/node from queue and add it to result
        current_node = queue.dequeue()
        #Get adjacent vertices to the current_node from the list,
        #and if they are not already visited then enqueue them in the Queue
        #and also update their distance from source by adding 1 in current_nodes's distance
        temp = g.array[current_node].head
        while (temp != None):
            if (not visited[temp.data]):
                queue.enqueue(temp.data)
                visited[temp.data] = True
                distance[temp.data] = distance[current_node] + 1
            temp = temp.next
    #end of while
    return distance[destination]

g = Graph(6)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(3,5)
g.addEdge(5,4)
g.addEdge(2,4)

distance = findMin(g, 0, 4)
g.printGraph()
print(distance) # 2





