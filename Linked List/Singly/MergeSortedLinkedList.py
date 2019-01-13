class Node:
    def __init__(self,key):
        self.next = None
        self.data = key
#----------------------------------------------------
# Given two sorted linked lists, merge them such that
# resulting linked list is also sorted.
# head1 -> 4 ->8 -> 15 -> 19 -> null
# head2 -> 7 -> 9 -> 10 ->16 -> null
# head1 -> 4 -> 7 -> 8 -> 9 -> 10 -> 15 -> 16 -> 19 -> Null
# Linear, O(m + n) where m and n are lengths of both linked lists.

def merge_sorted(head1, head2):
  # if both lists are empty then merged list is also empty
  # if one of the lists is empty then other is the merged list
  if head1 == None:
      return head2
  elif head2 == None:
      return head1

  mergedHead = None
  if head1.data <= head2.data:
      mergedHead = head1
      head1 = head1.next
  else:
      mergedHead = head2
      head2 = head2.next

  mergedTail = mergedHead
  
  while head1 != None and head2 != None:
      temp = None
      if head1.data <= head2.data:
          temp = head1
          head1 = head1.next
      else:
          temp = head2
          head2 = head2.next

      mergedTail.next = temp
      mergedTail = temp

  if head1 != None:
      mergedTail.next = head1
  elif head2 != None:
      mergedTail.next = head2

  return mergedHead

n1 = Node(4)
n2 = Node(8)
n3 = Node(15)
n4 = Node(19)
n1.next = n2
n2.next = n3
n3.next = n4

n11 = Node(7)
n22 = Node(9)
n33 = Node(10)
n44 = Node(16)
n11.next = n22
n22.next = n33
n33.next = n44

node = merge_sorted(n1, n11)

current = node
while(current!=None):
    print(current.data, end = ' ') # 4 7 8 9 10 15 16 19
    current= current.next