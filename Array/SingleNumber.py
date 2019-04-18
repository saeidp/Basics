# in an array of integers. All numbers occur twice except one number which occurs once. 
# Find the number in O(n) time & constant extra space.

# Example:

# Input:  ar[] = {7, 3, 5, 4, 5, 3, 4};
# Output: 7 
# One solution is to check every element if it appears once or not. Once an an element 
# with single occurrence is found, return it. Time complexity of this solution is O(n2).

# A better Solution
#1) Traverse all elements and put them in a hash table. Element is used as key and count
# of occurrences is use value in hash table.
#2) Traverse the array again and print the element with count 1 in hash table.
# This solution works in O(n) time, but requires extra space.
def findSingleNumberHashTable(arr):
    hashTable = {}
    for i in range(len(arr)):
        k = arr[i] 
        if  k in hashTable:
            hashTable[k] += 1
        else:
            hashTable[k] = 1
    for k,v in hashTable.items():
        if v == 1:
            return k
    return -1

arr = [7, 3, 5, 4, 5, 3, 4]
print(findSingleNumberHashTable(arr))


# The best Solution
# a) XOR of a number with itself is 0.
# b) XOR of a number with 0 is number itself.
#res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4

#Since XOR is associative and commutative, above 
#expression can be written as:
#res = 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)  
 #   = 7 ^ 0 ^ 0 ^ 0
 #   = 7 ^ 0
 #   = 7 
def findSingleNumber(a, n):
    result = 0
    for i in range(n):
        result ^= a[i]
    return result

print(findSingleNumber([7, 3, 5, 4, 5, 3, 4], 7)) # 7
