class Node:
    def __init__(self,key):
        self.next = None
        self.data = key

# it uses recursion but it just prints them all
def printkthToLast(head, k):
    if head == None:
        return 0
    index = printkthToLast(head.next, k) + 1
    if index == k:
        print(str(k) + "th to last node is " + str(head.data))
    return index

node0 = Node(22)
node1 = Node(18)
node2 = Node(60)
node3 = Node (78)
node4 = Node (47)
node5 = Node (39)
node6 = Node (99)

node0.next = node1
node1.next =  node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None 

printkthToLast(node0, 3)
#-------------------------------------
# In this approach we create a wrapper just to make sure we can track the index because
# we couldn't simultaneously return a counter and an index. we wrap the counter in a class index
class Index:
    def __init__(self):
        self.value = 0

def findKthToLast(head, k):
    idx = Index()
    return findKth(head, k, idx)


def findKth(head, k, idx):
    if head == None:
        return None
    node = findKth(head.next, k, idx)
    idx.value = idx.value + 1
    if idx.value == k:
        return head
    return node

current = findKthToLast(node0, 3)
print(current.data)

# ----------------------------------------------------------
# third approach O(n) and memory O(1) is two pointers
# The idea is to have two pointers n nodes apart: one pointing to the head and the other
# pointing to the nth node. Then we move both pointers forward until the second pointer 
# reaches the tail. Now the first pointer will be pointing to the nth node from last. 
# And if we reach the tail before making both pointers nnodes apart, that means n is out of bounds
def find_nth_from_last(head, n):
    if(head == None or n < 1):
        return None

    #we will use two pointers head and tail
    # where head and tail are 'n' nodes apart.
    tail = head

    while(tail != None and n > 0):
        tail = tail.next
        n -=1

    # check out of bounds
    if(n !=0):
        return None
    
    # When tail pointer reaches the end of 
    # list, head is pointing at nth node

    while(tail !=None):
        tail= tail.next
        head = head.next

    return head

current = find_nth_from_last(node0, 3)
print(current.data)



