# The shell sort improves on the insertion
# sort by breaking the original list into a
# number of smaller sublists, each of which is
# sorted using an insertion sort. The unique way
# that these sublists are chosen is the key to
# the shell sort. Instead of breaking the list
# into sublists of contiguous items, the shell
# sort uses an increment i, sometimes called
# the gap, to create a sublist by choosing all
# items that are i items apart.
def shellSort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for start in range(gap):
            gapInsertionSort(arr, start, gap)
        gap = gap // 2

def gapInsertionSort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        currentValue = arr[i]
        position = i
        while position >= gap and arr[position - gap] > currentValue:
            arr[position] = arr[position - gap]
            position -= gap
        arr[position] = currentValue

arr = [45,67,23,45,21,24,7,2,6,4,90]
shellSort(arr)
print(arr)
