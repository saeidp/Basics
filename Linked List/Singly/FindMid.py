class Node:
    def __init__(self,key):
        self.next = None
        self.data = key
    
# you have to implement findMid() function which
# will take a linked-list as an input and returns
# the middle element of the list. linkedlist = 7->14->10->21
# mid = 14
# linkedList = 7->14->10->21->22  then mid = 10

# we move mid node one step at a time but current two steps
# when current reaches at end
def findMid(head):
    if(head == None):
        return None
    
    current = head
    if(current.next == None):
        return current
    
    mid = current
    current = current.next.next
    while(current != None):
        mid = mid.next
        current = current.next
        if(current != None):
            current = current.next
    if(mid != None):
        return mid
    return None

node0 = Node(7)
node1 = Node(14)
node2 = Node(10)
node3 = Node (21)
node0.next = node1
node1.next =  node2
node2.next = node3
node3.next = None 

mid = findMid(node0)
print (mid.data)

node4 = Node (22)
node3.next = node4
node4.next = None 

mid = findMid(node0)
print (mid.data)

# (Slower) This solution traverse the linke list two times
# it finds the length and then mid length and in the
# second traverse check the mid to find the node 
def findMidUsingLength(head):
    if(head == None):
        return None
    current = head
    length = 0
    while(current != None):
        length += 1
        current = current.next
    if(length % 2 == 0):
        midLength = length //2
    else:
        midLength = length // 2 + 1

    current = head
    length = 0
    while(current !=None):
        length +=1
        if (length == midLength):
            return current
        current = current.next
    return None


node0 = Node(7)
node1 = Node(14)
node2 = Node(10)
node3 = Node (21)
node0.next = node1
node1.next =  node2
node2.next = node3
node3.next = None 

mid = findMidUsingLength(node0)
print (mid.data)

node4 = Node (22)
node3.next = node4
node4.next = None 

mid = findMidUsingLength(node0)
print (mid.data)