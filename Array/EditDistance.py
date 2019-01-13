# Check if edit distance between two strings is one An edit between two strings
# is one of the following changes.
# Add a character
# Delete a character
# Change a character
# Given two string s1 and s2, find if s1 can be converted to s2 with exactly
# one edit. Expected time complexity is O(m+n) where m and n are lengths of two
# strings.
# Input:  s1 = "geeks", s2 = "geek"
# Output: yes
# Number of edits is 1
def isEditDistanceOne(s1, s2): 
    # Find lengths of given strings 
    m = len(s1) 
    n = len(s2) 
  
    # If difference between lengths is more than 1, 
    # then strings can't be at one distance 
    if abs(m - n) > 1: 
        return False 
    count = 0    # Count of isEditDistanceOne 
    i = 0
    j = 0
    while i < m and j < n: 
        # If current characters dont match 
        if s1[i] != s2[j]: 
            if count == 1: 
                return False 
            # If length of one string is 
            # more, then only possible edit 
            # is to remove a character 
            if m > n: 
                i+=1
            elif m < n: 
                j+=1
            else:    # If lengths of both strings is same 
                i+=1
                j+=1
  
            # Increment count of edits 
            count+=1
  
        else:    # if current characters match 
            i+=1
            j+=1
  
    # if last character is extra in any string 
    if i < m or j < n: 
        count+=1
  
    return count == 1

s1 = "gfg"
s2 = "gf"
print(isEditDistanceOne(s1, s2))