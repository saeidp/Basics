# given a list, find two pairs such that their sum is equal
# a+b=c+d, You only have to find first two pairs in the list 
# which satisfies the above condition
# my_list = [3, 4, 7, 1, 12, 9]
# Output: "[4,12],[7,9]"

#Create HashMap with Key being sum and value being a pair
#  i.e key = 3 , value = {1,2}
#Traverse all possible pairs in my_list and store sums in
# map. If sum already exist then print out the two pairs.
def findPair(my_list):
    result = ""
    hMap = dict()
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            sum = my_list[i] + my_list[j] #calculate sum
            if (not sum in hMap):
                #If sum is not present in Map then insert it alongwith pair
                hMap[sum]  = [my_list[i],my_list[j]]
            else:
                #Sum already present in Map
                prev_pair = hMap.get(sum)
                #Since list elements are distinct, we don't
                #need to check if any element is common among pairs
                result += "[" + str(prev_pair[0]) + "," + str(prev_pair[1]) + "][" + str(my_list[i]) + "," + str(my_list[j]) + "]"
                return result
    return result

my_list = [3,4,7,1,12,9]
result = findPair(my_list)
print(result) # [4,12][7,9]