# sort the elements such that all the negative
# elements appear at left and positive elements
# appear at the right. [10,-1,20,4,5,-9,-6] ->
# [-1,-9,-6,10,20,4,5]
# We can fill newArray with negative
# and then positive using two loops but easier is 
# to use the arr for the negative. in this case
# we save one loop

# O(n) and memory O(n)
def reArrange(arr):
    newArray = []
    k = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[k] = arr[i]
            k +=1
        else:
            newArray.append(arr[i])
    for i in range(len(newArray)):
        arr[k] = newArray[i]
        k +=1
arr = [10, -1, 20, 4, 5, -9, -6]
reArrange(arr)
print(arr)

