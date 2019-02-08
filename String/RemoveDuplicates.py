# Remove duplicate characters from a string
# Given a string that contains duplicate occurrences of characters, remove these duplicate occurrences. 
# For example, if the input string is "abbabcddbabcdeedebc", after removing duplicates it should become "abcde".
# Runtime o(n) and memory O(n)

# this solution uses extra memory
# to keep all characters present in string.
def remove_duplicates(s):
    result = []
    for item in s:
        if item not in result:
            result.append(item)
    return ''.join(result)

s = "abbabcddbabcdeedebc"
print(remove_duplicates(s))