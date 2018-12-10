# Given a list, return a list where each index stores product of all numbers except the 
# number on the index itself.
def findProduct(arr):
  result = []
  if len(arr) == 1:
    result.append(0)
    return result
  for i in arr:
    product = 1
    for j in arr:
      if(i != j):
        product *= j
    result.append(product)
  return result

print(findProduct([1, 2, 3, 4])) # [24, 12, 8, 6]
