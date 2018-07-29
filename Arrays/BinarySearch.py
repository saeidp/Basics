def binarySearch(array, targetValue):
  min = 0
  max = len(array) -1
  while(min <= max):
    mid = min + (max - min) // 2
    if(array[mid] == targetValue):
      return mid
    elif(targetValue < array[mid]):
      max = mid - 1
    else:
      min = mid + 1
  return -1 
# print(binarySearch([1,2,3], 1))
print("Hello")