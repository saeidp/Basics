# Right Rotate the List by One Index
# n this problem, you have to implement rotateArray()
# function which will pick the last index from the right
# and rotate it to the left. Means the right-most element
# will appear at the left-most position in the list and so on.
# But in this problem, you only have to rotate by one element
# from the right. [1,2,3,4,5] --> [5, 1, 2, 3, 4]

# We will pick the last element which is 5 in this case
# and store it in a temporary value, then shift the whole
# list to the right starting from the first end.
# By the end, the first index will be free where you will
# store the last element.
def rotateArray(arr):
    index = len(arr) - 1
    temp = arr[index]
    for i in range(index, 0  , -1):
        arr[i] = arr[i -1]
    arr[0] = temp

arr = [1,2,3,4,5]
rotateArray(arr)
print(arr)

def rotateArray2(arr):
    index = len(arr) - 1
    temp = arr[index]
    j = index
    while(j > 0):
        arr[j] = arr[j -1]
        j -= 1
    arr[0] = temp

arr = [1,2,3,4,5]
rotateArray2(arr)
print(arr)
    



