# implement max min function which will re-arrange the elements
# and in such a way that the first position will have the
# largest number, the second will have the smallest, and the
# third will have second largest and so on.
# [1,2,3,4,5] --> [5, 1, 4, 2, 3]
# o(logn)
def maxMinSortedArray(arr):
    result = [-1] * len(arr)
    i=0
    j= len(arr) -1
    k = 0
    flag = True
    while k < len(arr):
        if flag:
            result[k] = arr[j]
            j -=1
        else:
            result[k] = arr[i]
            i +=1
        k +=1
        flag = not flag
    
    for i in range(len(arr)):
        arr[i] = result[i]
    
arr =  [1,2,3,4,5]
maxMinSortedArray(arr)
print(arr)


# This can max min any array not just sorted ones
# [1,3,2,4,6,7,5] -> [7, 1, 6, 2, 5, 3, 4]
# o(nlogn)
def maxMinArray(arr):
    arrMax = []
    arrMin = []

    arrMin = sorted(arr)
    arrMax = sorted(arr, reverse = True)
    i = 0
    j = 0
    k = 0
    n = len(arr)
    while k < n:
        arr[k] = arrMax[i]
        k +=1
        i +=1
        if k < n:
            arr[k] = arrMin[j]
            k +=1
            j +=1        

arr =  [1,2,3,4,5]
maxMinArray(arr)
print(arr)
   
arr =  [1,3,2,4,6,7,5]
maxMinArray(arr)
print(arr)        