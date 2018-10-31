#Given a sorted array, remove the duplicates in place
# such that each element appear only once and return 
# the new length.Given input array nums = [1,1,2], 
# Your function should return length = 2. It doesn't matter
#  what you leave beyond the new length
# o(n) and space o(1)
def removeDuplicate(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


print(removeDuplicate([0,1,2,2,3])) // 4

