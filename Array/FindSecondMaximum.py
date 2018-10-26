#Returns second maximum value from given list
def findSecondMaximum(arr):
    """Keep track of Maximum value, whenever a list index is greater
	than current Maximum value then make that max value 2nd max value and
	make that index value maximum value. It is assumed that the list is positive"""
    if(len(arr) == 0):
        return -1
    secondMax = -1
    max = arr[0]
    for i in range(1,len(arr)):
        if(arr[i] > max):
            secondMax = max
            max = arr[i]
        elif(arr[i] < max and arr[i] > secondMax):
            secondMax = arr[i]
    return secondMax

secondMax = findSecondMaximum([1,2,2])
print(secondMax)



