def findFirstUnique(arr):
    """Given a list, find the first integer which is 
    unique in the list.
    Unique means the number does not repeat
    and appears only once in the whole list
    2,3,6,6,3,7,3,2  -> 7
    """
    for i in range (len(arr)):
        Unique = True
        for j in range(len(arr)):
            if i!= j and arr[i] == arr[j]:
                Unique = False
                break

        if(Unique):
            return arr[i]
    return -1


index = findFirstUnique([2,3,6,6,3,7,3,2])
print(index) # -> 7


