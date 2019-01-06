#O(n), o(n)
def reverseWords(s):
    if s==None or len(s) == 0:
        return ""
    arr = s.split()
    sb =[]
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != "":
            sb.append(arr[i])
            if i !=0:
                sb.append(" ")
    return ''.join(sb)


s = reverseWords("the sky is blue")
print(s)

#----------------------------------
# geeksforgeeks O(n), o(1)
def reverseWords2(input): 
      
    # split words of string separated by space 
    inputWords = input.split(" ") 
  
    # reverse list of words 
    # suppose we have list of elements list = [1,2,3,4],  
    # list[0]=1, list[1]=2 and index -1 represents 
    # the last element list[-1]=4 ( equivalent to list[3]=4 ) 
    # So, inputWords[-1::-1] here we have three arguments 
    # first is -1 that means start from last element 
    # second argument is empty that means move to end of list 
    # third arguments is difference of steps 
    inputWords=inputWords[-1::-1] 
  
    # now join words with space 
    output = ' '.join(inputWords) 
      
    return output 

s = reverseWords2("the sky is blue")
print(s)
