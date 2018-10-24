#Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 
#'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of
#  single or double letters. For instance, it is okay for 'AAB' to return
# 'A2B1' even though this  technically takes more space.
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
def compress(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """
    # Begin Run as empty string
    run = ""
    length = len(s)
    
    # Check for length 0
    if length == 0:
        return ""
    
    # Check for length 1
    if length == 1:
        return s + "1"
    
    #Intialize Values
    count = 1
    i = 1
    while i < length:
        # Check to see if it is the same letter
        if s[i] == s[i - 1]: 
            # Add a count if same as previous
            count += 1
        else:
            # Otherwise store the previous data
            run = run + s[i - 1] + str(count)
            count = 1
        # Add to index count to terminate while loop
        i += 1
    # Put everything back into run
    run = run + s[i - 1] + str(count)
    
    return run

run = compress("AAB")
print(run)