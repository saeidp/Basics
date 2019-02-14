class Node:
    def __init__(self,key):
        self.next = None
        self.data = key
# O(n) , O(n)
# Input: list1 = 10->20->80->60 , 
# list2 = 15->20->30->60->45
# intersection: 20, 60
def intersection(head1, head2):
    if head1 == None and head2 == None:
        return None
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    current2 = head2
    visited = set()
    while current2 != None:
        visited.add(current2.data)
        current2 = current2.next

    current1 = head1
    head = None
    while current1 != None:
        if(current1.data in visited):
            new_node = Node(current1.data)
            if head is None:
                head = new_node
            else:
                last = head
                while (last.next):
                    last = last.next
                last.next = new_node
        current1 = current1.next
    
    return head

node0 = Node(10)
node1 = Node(20)
node2 = Node(80)
node3 = Node (60)
node0.next = node1
node1.next =  node2
node2.next = node3
node3.next = None 

node00 = Node(15)
node11 = Node(20)
node22 = Node(30)
node33 = Node(60)
node44 = Node(45)
node00.next = node11
node11.next =  node22
node22.next = node33
node33.next = node44
node44.next = None 
            
head = intersection(node0, node00)
current = head
while current != None:
    print(current.data, end= " ") #20, 60
    current = current.next
