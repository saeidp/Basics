class Node:
    def __init__(self,key):
        self.next = None
        self.data = key

def detectLoopUsingDictionary(head):
    if(head == None or head.next == None):
        return False
    s = set()
    current = head
    while (current != None):
        if current.data in s:
            return True
        else:
            s.add(current.data)
        current = current.next
    return False

# If slow_p and fast_p meet at some point then there is a loop 
def detectLoop(head):
    slow_p = fast_p = head
    while(slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next

        if(slow_p == fast_p):
            return True
    return False

        

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

# makes the loop
node3.next = node1

flag = detectLoopUsingDictionary(node1)
print(flag)

flag = detectLoop(node1)
print(flag)




