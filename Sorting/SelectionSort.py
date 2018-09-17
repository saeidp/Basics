# First, find the smallest item in the array, 
# and exchange it with the first entry. Then, find the
# next smallest item and exchange it with the second
# entry. Continue in this way until the entire array is
# sorted. This method is called selection sort because it
# works by repeatedly selecting the smallest remaining 
# item (N-1) + (N-2) + …1+ 0 

def selectionSort(array):
    n = len(array)
    for i in range(n - 1):
        min = i
        for j in range(i + 1 , n):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]

array = [10,12,5,11,3]
selectionSort(array)
print(array)
