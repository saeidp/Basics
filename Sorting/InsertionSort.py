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

array = [2,7,8,5,4,3,1]
insertionSort(array)
print(array)

# The insertion sort always maintains a sorted sublist
# in the lower positions of the list.
# Each new item is then “inserted” back into the previous
# sublist such that the sorted sublist is one item larger.
# We begin by assuming that a list with one item (position 0)
# is already sorted.
# On each pass, one for each item 1 through n−1, the current
# item is checked against those in the already sorted
# sublist.
# As we look back into the already sorted sublist, we shift
# those items that are greater to the right.
# When we reach a smaller item or the end of the sublist,
# the current item can be inserted.
def insertionSort2(arr):
    for i in range(1, len(arr)):
        currentValue = arr[i]
        position = i
        while position > 0 and arr[position - 1] > currentValue:
            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = currentValue


array = [2,7,8,5,4,3,1]
insertionSort2(array)
print(array)

