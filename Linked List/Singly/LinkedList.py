# GeeksforGeeks
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


llist = LinkedList()
# Insert 6.  So linked list becomes 6->None
llist.insertAtTail(6)
# Insert 7 at the beginning. So linked list becomes 7->6->None
llist.insertAtHead(7)
# Insert 1 at the beginning. So linked list becomes 1->7->6->None
llist.insertAtHead(1)
# Insert 4 at the end. So linked list becomes 1->7->6->4->None
llist.insertAtTail(4)
# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
llist.insertAfter(llist.head.next, 8)
print('Created linked list is:', end=' ')
llist.printList()

llist.deleteNode(6)
print("\nLinked List after Deletion of 6:", end=' ')
llist.printList()