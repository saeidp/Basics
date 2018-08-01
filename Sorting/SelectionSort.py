def selectionSort(array):
    n = len(array)
    for i in range(n):
        minIndex = indexOfMinimum(array, i)
        swap(array, i, minIndex)
    return array

def swap(array, first_index, second_index):
    array[first_index], array[second_index] = array[second_index], array[first_index]
    return array
  
def indexOfMinimum(array, startIndex):
    minValue = array[startIndex]
    minIndex = startIndex
    for i in range(startIndex + 1,len(array)):
        if(array[i] < minValue):
            minValue = array[i]
            minIndex = i
    return minIndex

array = [10,12,5,11,3]
print(selectionSort(array))
