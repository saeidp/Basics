# If you are given a nested list, can you find symmetric pair in that list
# By definition, (a,b) and (c,d) are symmetric pairs if, a = c and b = d.
# my_list = [[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]
# Output -> [3,4] [5,9]
def findSymmetric(my_list):
    #Create an empty Hash Map
    #Traverse given list
    #Look for second element of each pair in the hash. 
    # i.e for pair (1,2) look for key 2 in map.
    #If found then store it in the result list, otherwise insert
    # the pair in hash
    dictionary = dict()
    result = ""
    #Traverse through the given list
    for i in range(len(my_list)):
        first = my_list[i][0]
        second = my_list[i][1]
        value = dictionary.get(second)
        if(value != None and value == first):
            #Symmetric Pair found
            result += "[" + str(second) + "," + str(first) + "]"
        else:
            dictionary[first] = second
    return result


my_list = [[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]
print(findSymmetric(my_list)) # [3,4] [5,9]