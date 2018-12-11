# Given a null terminated string, remove any white spaces (tabs or spaces). 
def removeSpaces(s):
    list= []
    for i in range(len(s)):
        if s[i] != ' ':
            list.append(s[i])
    return ''.join(list)

string = " All greek  to    me.  "
print(removeSpaces(string)) # Allgreektome.