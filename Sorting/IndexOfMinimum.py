#Find Minimum in Subarray
def indexOfMinimum(array, startIndex):
    minValue = array[startIndex]
    minIndex = startIndex
    for i in range(startIndex + 1,len(array)):
        if(array[i] < minValue):
            minValue = array[i]
            minIndex = i
    return minIndex

minIndex = indexOfMinimum([2,4,3], 0)   
print(minIndex)



    
    
    
 