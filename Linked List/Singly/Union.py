class Node:
    def __init__(self,key):
        self.next = None
        self.data = key

# Union of two linked list
# Input: list1 = 10->20->80->60 , list2 = 15->20->30->60->45
# Output: Union = 10->20->80->60->15->30->45

def union(head1, head2):
  
    if head1 == None and head2 == None:
        return None
    if head1 == None:
        return head2
    if head2 == None:
        return head1
   
    visited = []

    last1 = head1
    while last1.next != None:
        visited.append(last1.data)
        last1 = last1.next
    visited.append(last1.data)
    current2 = head2
    while current2 != None:
        if current2.data not in visited:
            last1.next = current2
            last1 = last1.next
        current2 = current2.next
    last1.next = None
    return head1
    
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


head = union(node0, node00)
current = head
while current != None:
    print(current.data, end= " ")
    current = current.next
print() 