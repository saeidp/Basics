def isArraySorted(a, index):
    if index == 1:
        return True   
    if a[index - 1] < a[index - 2]:
        return False
    else:
        return isArraySorted(a, index - 1)


a = [2, 3, 4]
print(isArraySorted(a, 3)) # True

a = [2, 3, 4, 1]
print(isArraySorted(a, 4)) # False
    