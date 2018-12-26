
# Given a 32-bit signed integer, reverse digits of an integer.
# Input: 123
# Output: 321

# Input: -123
# Output: -321

# Input: 120
# Output: 21

# Input: 1534236469
# Output: 0

# range: [−231,  231 − 1].
def reverse(x):
    
    """
    :type x: int
    :rtype: int
    """
    arr = list(str(x))
    if arr[0] == '-':
        arr.remove('-')
        arr.append('-')

    reversedValue = ""
    for _ in range(len(arr)):
        reversedValue += arr.pop()
    out = int(reversedValue)
    if out < -2**31 or out > 2**31 -1:
        out = 0
    return out

arrout = reverse(1534236469)
print(arrout) # 0

#------------------------------------------

class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        list_=list(str(x))
        i=0
        j=len(list_)-1
        while i<j : 
            if list_[i]=="-":
                i+=1
            
            temp=list_[i]
            list_[i]=list_[j]
            list_[j]=temp
            
            i+=1
            j-=1
        req_num=int ("".join(list_))

        max_= 2**31 - 1
        min_=-1 * 2**31
        if ((req_num > max_) or (req_num < min_)):
            return 0 
        
        return req_num