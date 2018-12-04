# If you are given two lists list1 and list2, can you
# check if these lists are disjoint?
# Disjoint lists mean that their intersection
# returns nothing or there are no common elements in them
# The assumption is that there are no duplicate elements in each list
# list1 = [9,4,3,1,-2,6,5]
# list2 = [7,10,8]
# output -> true
def isDisjoint(list1,list2):
  s = set(list1)
  for i in range(len(list2)):
    if list2[i] in s:
      return False 
  return True

list1 = [9, 4, 3, 1, -2, 6, 5]
list2 = [7, 10, 8]

print(list1, list2)
print(isDisjoint(list1, list2)) # True

