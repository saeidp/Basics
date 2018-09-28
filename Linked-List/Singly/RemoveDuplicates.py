class Node:
    def __init__(self,key):
        self.next = None
        self.data = key

# This function will take a linkedlist as input and remove all the elements that appear
# more than once in the list.  linkedlist = 1->2->2->2->3->4->4->5->6    :   1->2->3->4->5->6
def removeDuplicates(head):
    if(head == None):
        return None
    if head.next == None:
        return head

    visitedNodes = set()
    visitedNodes.add(head.data)
    current = head.next
    previous = head

    while current != None:
        if current.data in visitedNodes:
            previous.next = current.next
        else:
            visitedNodes.add(current.data)
            previous = current
        current = current.next
    
    return head
  

node0 = Node(1)
node1 = Node(2)
node2 = Node(2)
node3 = Node(2)
node4 = Node(3)
node5 = Node(4)
node6 = Node(4)
node7 = Node(5)
node8 = Node(6)

node0.next = node1
node1.next =  node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6 
node6.next = node7 
node7.next = node8 
node8.next = None 

head = removeDuplicates(node0)
current = head
while current != None: 
    print(current.data,end=" ")
    current = current.next
