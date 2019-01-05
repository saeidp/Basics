# Given an array of integers (positive and negative) find the largest
# continuous sum.
def find_max_sum_sub_array(A):
  if len(A) < 1:
    return 0

  curr_max = A[0]
  global_max = A[0]
  lengthA = len(A)
  for i in range(1, lengthA):
    if curr_max < 0:
      curr_max = A[i]
    else:
      curr_max += A[i]

    if global_max < curr_max:
      global_max = curr_max

  return global_max
print(find_max_sum_sub_array([1,2,-1,3,4,10,10,-10,-1])) #29
#------------------------------------------------
def large_cont_sum(arr):
    if len(arr)==0:   # Check to see if array is length 0
        return 0
    
    # Start the max and current sum at the first element
    max_sum=current_sum=arr[0] 
    
    # For every element in array
    for num in arr[1:]: 
        
        # Set current sum as the higher of the two
        current_sum=max(current_sum+num, num)
        
        # Set max as the higher between the currentSum and the current max
        max_sum=max(current_sum, max_sum)
    return max_sum

print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1])) #29


