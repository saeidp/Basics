# Find whether a list is a subset of another list by using built-in hashtable
# list1 = [9,4,7,1,-2,6,5], list2 = [7,1,-2]
# Output -> true
def isSubset(list1, list2):
    s = set(list1)
    for i in range(len(list2)):
        if not list2[i] in s:
            return False
    return True

list1 = [9, 7, 1, -2, 6, 5]
list2 = [7, 1, -2]

print(list1, list2)
print(isSubset(list1, list2)) # True
