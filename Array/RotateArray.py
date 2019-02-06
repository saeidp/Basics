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
#-------------------------------------------
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
#-------------------------------------------
# if rotate for k elements and in o(n) and o(n) space
# The above algorith is not useful as it exceed limit of time
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    index = len(nums) - 1
    arr = []
    for i in range(k):
        arr.insert(0, nums[index - i])
    for j in range (0, len(nums) - k):
        arr.append(nums[j])
    for i in range(len(nums)):
        nums[i] = arr[i]
    

nums =  [1,2,3,4,5]
rotate(nums, 1)
print(nums)
#-------------------------------------------------

# Original List                   : 1 2 3 4 5 6 7
# After reversing all numbers     : 7 6 5 4 3 2 1
# After reversing first k numbers : 5 6 7 4 3 2 1
# After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
# O(n) and o(1) space
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end += 1

def rotate2(nums, k):
    k %= len(nums) # to make sure k is not larger than the array
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)

nums =  [1,2,3,4,5]
rotate(nums, 1)
print(nums)

