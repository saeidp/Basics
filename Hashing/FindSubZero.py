# Given a list with positive and negative integers, extract
# a sub-list from it which adds up to zero
# my_list = [6, 4, -7, 3, 12, 9}]
# output: true -> 4 - 7 + 3 = 0

# Use HashMap to store sum as key and index i as value
# till sum has been calculated
# Traverse the list and return true if either 
# my_list[i] == 0 or sum == 0 or HashMap already contains 
# the sum. If you completely traverse the list and havent
# found any of the above three #conditions then simply 
# return false
  
def findSubZero(my_list):
    hMap = dict()
    sum = 0
    #Traverse through the given list
    for i in range(len(my_list)):
        sum += my_list[i]
        if (my_list[i] == 0 or sum == 0 or hMap.get(sum) != None):
            return True
        hMap[sum] = i
    return False

my_list = [6, 4, -7, 3, 12, 9]
result = findSubZero(my_list)
print(result) # True
