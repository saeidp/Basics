#Find Two Numbers that Adds up to "n"
def findTwoSum(arr, value):
  for i in range(len(arr)):
    member = value - arr[i]
    for j in range(i+1, len(arr), 1):
      if(arr[j]== member):
        return [arr[i], arr[j]]
  return []
