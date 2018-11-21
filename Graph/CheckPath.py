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
#------------------------------------------------------
# Check if a path exists betwee veritices
# Given a graph and two vertices, can you
# write a code to check if a path exists between the two given vertices? 
#graph = {
#    0 -> 2
#    0 -> 5
#    2 -> 3
#    2 -> 4
#    5 -> 3
#    5 -> 6
#    3 -> 6
#    6 -> 7
#    6 -> 8
#    6 -> 4
#    7 -> 8
#}

#source = 0
#destination = 7
#True
# 0->5->6->7
# 0->2->3->6->7
# 0->5->3->6->7 

#Perfrom DFS Traversal starting from source and if you reach destination
#then it means that there exist a path between source and destination 
#so return true and if you traverse the graph but can't reach destination
#then simply return false
def checkPath(g, source, destination):
    #A list to hold the history of visited nodes (by default all false)
    #Make a node visited whenever you push it into stack
    visited = []
    for _ in range(g.vertices):
        visited.append(False)
    #Create Stack
    stack =  Stack()
    stack.push(source)
    visited[source] = True
    #Traverse while stack is not empty
    while (stack.isEmpty() == False):
        #Pop a vertex/node from stack
        current_node = stack.pop()
        #Get adjacent vertices to the current_node from the list,
        #and if only push unvisited adjacent vertices into stack
        #Before pushing into stack, check if it's the destination
        temp = g.array[current_node].head
        while (temp != None):
            if (visited[temp.data] == False):
                if (temp.data == destination):
                    return True
                stack.push(temp.data)
                visited[temp.data] = True
            temp = temp.next
    return False   

g = Graph(9)
g.addEdge(0,2)
g.addEdge(0,5)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(5,3)
g.addEdge(5,6)
g.addEdge(6,7)
g.addEdge(6,8)
g.addEdge(6,4)
g.addEdge(7,8)

print(checkPath(g, 0, 7))


