# Once the mergeSort function is invoked on the left half
# and the right half, it is assumed they are sorted. The
# rest of the function is responsible for merging the two
# smaller sorted lists into a larger sorted list. Notice 
# that the merge operation places the items back into the
# original list (alist) one at a time by repeatedly taking
# the smallest item from the sorted lists.
# A merge sort is an O(nlogn) algorithm. logn for dividing 
# to half and n for meging them back
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) //2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i +=1
            else:
                arr[k] = rightHalf[j]
                j +=1
            k +=1
        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i +=1
            k +=1
        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j +=1
            k +=1
arr = [11,2,5,4,7,6,8,1,23]
mergeSort(arr)
print(arr)
