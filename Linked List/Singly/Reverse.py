class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#input: 0->1->2->3->4->5->None
#output: 6->5->4->3->2->1->None
def reverse2(head):
    if head == None:
        return None
    head1 = Node(head.data)
    current = head.next
    while(current != None):
        node = Node(current.data)
        node.next = head1
        head1 = node
        current = current.next
    return head1

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node0.next = node1
node1.next =  node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None 

temp = reverse2(node0)
while(temp.next != None):
    print(temp.data, "->", end=" ")
    temp = temp.next
print(temp.data, "-> None")
#---------------------------------------------------------
def reverse(head):
  prev = None #To keep track of the previous element, will be used in swapping links
  current = head #firstElement
  next = None
  #While Traversing the list, swap links
  while (current != None):
    next = current.next
    current.next = prev
    prev = current
    current = next
  #Linking Head Node with the new First Element
  head = prev
  return head

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node0.next = node1
node1.next =  node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None 

temp = reverse(node0)
while(temp.next != None):
    print(temp.data, "->", end=" ")
    temp = temp.next
print(temp.data, "-> None")
