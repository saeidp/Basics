import sys
#Find minimum value in a list
def findMinimum(array):
    n= len(array)
    min = sys.maxsize
    for i in range(n):
        if(array[i] < min):
            min = array[i]
    return min

min = findMinimum([3,4,5,2])
print(min)
