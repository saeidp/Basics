# An Anagram Detection Example. 
# One string is an anagram of another if the second is simply a rearrangement of the first. For example,
# 'heart' and 'earth' are anagrams. The strings 'python' and 'typhon' are anagrams as well. For the sake of simplicity,
# we will assume that the two strings in question are of equal length and that they are made up of symbols from the set
# of 26 lowercase alphabetic characters
def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    for k in range(26):
        if(c1[k] != c2[k]):
            return False
    return True

print(anagramSolution4('apple','pleaqp'))