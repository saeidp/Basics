# Remove duplicate characters from a string
# Given a string that contains duplicate occurrences of characters, remove these duplicate occurrences. 
# For example, if the input string is "abbabcddbabcdeedebc", after removing duplicates it should become "abcde".
# Runtime o(n) and memory O(n)

# this solution uses extra memory
# to keep all characters present in string.
def remove_duplicates_1(s):
    seen = set()
    result = []
    for item in s:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


s = "abbabcddbabcdeedebc"
s = remove_duplicates_1(s)
print(''.join(s))