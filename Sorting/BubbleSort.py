# The bubble sort makes multiple passes through a list.
# It compares adjacent items and exchanges those that are
# out of order. Each pass through the list places the next
# largest value in its proper place. In essence, 
# each item “bubbles” up to the location where it belongs.

def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j +1] = arr[j + 1], arr[j]

arr = [3,2,13,4,6,5,7,8,1,20]
bubbleSort(arr)
print(arr)
