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
    def push(self, new_data):

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
    def append(self, new_data):

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
# This implementation of the Graph uses adjacency list and
# it uses linked list and indexex of the information added to the graph
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []
        for _ in range(vertices):
            temp = LinkedList()
            self.array.append(temp)
    
    def addEdge(self, source, destination):
        self.array[source].push(destination)
    
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


def bfsTraversal(g):
    result = ""
    num_of_vertices = g.vertices
	#Alist to hold the history of visited nodes
	#Make a node visited whenever you enqueue it into queue
    visited = []
    for _ in range(num_of_vertices):
        visited.append(False)
    #Create Queue(implemented in previous lesson) for Breadth First Traversal and enqueue source in it
    queue = Queue()
    queue.enqueue(0)
    visited[0] = True
    #Traverse while queue is not empty
    while(queue.isEmpty() == False):
        #Dequeue a vertex/node from queue and add it to result
        index = queue.dequeue()
        result += str(index)
    	#Get adjacent vertices to the index from the list,
	    #and if they are not already visited then enqueue them in the Queue
        temp = g.array[index].head
        while (temp != None):
            if(visited[temp.data] == False):
                queue.enqueue(temp.data)
                visited[index] = True #Visit the current Node
            temp = temp.next
    return result #For the above graph it should return "01234" or "02143"

def dfsTraverse(g):
        result = ""
        num_of_vertices = g.vertices
        visited = []
        for _ in range(num_of_vertices):
            visited.append(False)
        stack = Stack()
        stack.push(0)
        visited[0] = True
        while stack.isEmpty() == False:
            item = stack.pop()
            result += str(item)
            temp = g.array[item].head
            while temp !=None:
                if(visited[temp.data] == False):
                    stack.push(temp.data)
                    visited[temp.data] = True
                temp = temp.next
        return result #For the above graph it should return 01342








# 0, 1, 2, 3, 4 are all indexes of the actual information we are creating a graph from
#i.e: Array["first", "second", "Third", "Forth", "Fifth"] you can create a graph as follows
# 0 means first and 1 ...
g =  Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)

g.printGraph()
#| 0 | => [ 2 ] -> [ 1 ] -> None
#| 1 | => [ 4 ] -> [ 3 ] -> None
#| 2 | => None
#| 3 | => None
#| 4 | => None

result = dfsTraverse(g)
print(result)