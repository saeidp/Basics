# Merge two sorted arrays in order
# MergeArrays([1,3,4,5] , [2,6,7,8]) -> [1,2,3,4,5,6,7,8]
def mergeArrays(arr1, arr2):
  i = 0
  j = 0
  k = 0
  n1 = len(arr1)
  n2 = len(arr2)
  arr = [-1] * (n1 + n2)
  
  while(i < n1 and j <  n2):
    if(arr1[i] < arr2[j]):
      arr[k] = arr1[i]
      i += 1
    else:
      arr[k] = arr2[j]
      j +=1
    k +=1

  while(i < n1 ):
    arr[k] = arr1[i]
    i += 1
    k +=1
  while(j <n2):
    arr[k] = arr2[j]
    j += 1
    k +=1
  return arr

arr = mergeArrays([1,3,4,5] , [2,6,7,8])

print(arr)