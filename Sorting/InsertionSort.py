# Implement Insertion Sort
def insertionSort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(i + 1, 0 , -1):
            if(array[j - 1] > array[j]):
                array[j - 1] , array[j] = array[j], array[j-1]
            else:
                break
    return array


array = insertionSort([2,7,8,5,4,3,1])
print(array)

