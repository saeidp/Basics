# Linked List head is Node(-1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#------------------------------------------------------
# input: 10-> 20-> 30-> 40
# output: 4
def linkedListLength(head):
    """
    Find Length of Linked List 
    """
    if head == None:
        return 0
    current = head
    length = 1
    while(current.next != None):
        length += 1
        current = current.next
    return length

node0 = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node (40)
node0.next = node1
node1.next =  node2
node2.next = node3
node3.next = None 

length = linkedListLength(node0)

print(length)
