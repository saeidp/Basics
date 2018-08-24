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