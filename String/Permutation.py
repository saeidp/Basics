# If two strings are permutations, then we know they have the same characters, 
# but in different orders. Therefore, sorting the strings will put the characters
# from two permutations in the same order. We just need to compare the sorted versions of the strings.
def permutation(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

isPermutation = permutation("abc", "cba")
print(isPermutation) # True