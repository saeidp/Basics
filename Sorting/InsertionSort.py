# Implement Insertion Sort
# On the first pass, it compares a maximum of one item.
# On the second pass, it’s a maximum of two items, 
# and so on, up to a maximum of N-1 comparisons on the last
# pass. This is 1 + 2 + 3 + … + N-1 = N*(N-1)/2
# However, because on each pass an average of only half of
# the maximum number of items are actually compared before
# the insertion point is found, we can divide by 2,
#which gives N*(N-1)/4. Insertion sort is almost 2 times
# the bubble sort but slightly better than selection sort
#O(N^2)

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

