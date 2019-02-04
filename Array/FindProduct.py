# Given a list, return a list where each index stores product of all numbers except the 
# number on the index itself.
def findProduct(arr):
  result = []
  for i in range(len(arr)):
    product = 1
    for j in range(len(arr)):
      if(i != j):
        product *= arr[j]
    result.append(product)
  return result

print(findProduct([1, 2, 3, 4])) # [24, 12, 8, 6]
