def binarySearch(array, key):
  min = 0
  max = len(array) -1
  while(min <= max):
    mid = min + (max - min) // 2
    if(array[mid] == key):
      return mid
    elif(key < array[mid]):
      max = mid - 1
    else:
      min = mid + 1
  return -1 
a = [1, 2, 3, 4, 5, 6]
index = binarySearch(a, 5)
print(index)

# Recursive Version of Binary Search
def binarySearchRecursive(array, key, low, high):
  if low > high:
    return -1
  mid = low + (high - low) // 2
  if(array[mid] == key):
    return mid
  elif(key < array[mid]):
    return binarySearchRecursive(array, key, low, mid - 1)
  else:
    return binarySearchRecursive(array, key, mid + 1, high)

def binarySearch2(array, key):
  return binarySearchRecursive(array, key, 0, len(array) -1)

a = [1, 2, 3, 4, 5, 6]
index = binarySearch2(a, 5)
print(index)

