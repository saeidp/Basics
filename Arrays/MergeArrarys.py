# Merge two arrays in order
# MergeArrays([1,3,4,5] , [2,6,7,8]) -> [1,2,3,4,5,6,7,8]
def mergeArrays(arr1, arr2):
  i = 0
  j = 0
  k = 0
  arr = []
  n1 = len(arr1)
  n2 = len(arr2)

  while(i < n1 and j <  n2):
    if(arr1[i] < arr2[j]):
      arr.append(arr1[i])
      i += 1
      k += 1
    else:
      arr.append(arr2[j])
      j +=1
      k += 1
  while(i < n1 ):
    arr.append(arr1[i])
    i += 1
  while(j <n2):
    arr.append(arr2[j])
    j += 1
  return arr

arr = mergeArrays([1,3,4,5] , [2,6,7,8])

print(arr)