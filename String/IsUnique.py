# Implement an algorithm to determine if a string has all unique
# characters.
# One solution is to create an array of boolean values, where 
# the flag at index i indicates whether character i in the
# alphabet is contained in the string. The second time you see
# this character you can immediately return false.
# We can also immediately return false if the string length 
# exceeds the number of unique characters in the alphabet. 
# After all, you can't form a string of 280 unique characters 
# out of a 128-character alphabet.
def isUniqueChars(str):
    if len(str) > 128: # assume Aschii
        return False
    charList = [False] * 128
    for i in range(len(str)):
        val = ord(str[i])
        if charList[val]:
            return False
        charList[val] = True
    return True

isUnique = isUniqueChars("abc") # true
print(isUnique)

isUnique = isUniqueChars("abcb") # False
print(isUnique)
