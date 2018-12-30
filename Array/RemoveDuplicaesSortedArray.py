#Given a sorted array, remove the duplicates in place
# such that each element appear only once and return 
# the new length.Given input array nums = [1,1,2], 
# Your function should return length = 2. It doesn't matter
#  what you leave beyond the new length
# o(n) and space o(1)
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    j = 0
    for i in range(1,len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return j + 1


print(removeDuplicates([0,1,2,2,3])) # 4

#-------------------------------------
def removeDuplicates2(nums):
    if len(nums) == 0:
        return 0
    n = len(nums) - 1
    i = 0
    j = 1
    
    while i < n:
        if nums[i] < nums[i + 1]:
            nums[j] = nums[i+1]
            j += 1
        i += 1
    return j
print(removeDuplicates2([0,1,2,2,3])) # 4
print(removeDuplicates2([1,1,2])) # 2


