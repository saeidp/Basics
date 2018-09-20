#//O(nlogn)
# Recursive solution has O(logn) memory complexity as
# it will consume memory on the stack.
# Here is an overview of how the quicksort algorithm
# works. Select a pivot element from the array.
# We can pick the first element as the pivot (following
# Hoare's algorithm). Another common approach is to select
# a random element as the pivot.
# Reorder the array by comparing with the pivot element
# such that smaller values end up at the left side, and
# the larger values end up at the right side of the pivot.
# Now, the pivot element is in its correct sorted position.
# Applying the above steps, we can recursively sort the
# sublists on the right and left sides of the pivot.
def quickSort(array):
    if(len(array) < 2):
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([10, 5, 2, 3, 8, 11, 1]))

# -------- Second Implementation ----------
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low,high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i +=1
    arr[i],arr[high] = arr[high], arr[i]
    return i    

def quickSortRec(a, l, h):
    if h > l:
        pivot = partition(a, l, h)
        quickSortRec(a, l, pivot -1)
        quickSortRec(a, pivot + 1, h)

def quickSort2(a):
    quickSortRec(a, 0, len(a) - 1)

array = [10, 5, 2, 3, 8, 11, 1]
quickSort2(array)
print(array)