# Generate all strings of n bits. Assume a[0,n-1] be an array of size n
# We will follow a backwards approach since it is a recursive function.

# For instance lets say n = 1,
# The method is called as binary(1); arr[n-1] is set as ‘0’ (arr[1-1] = arr[0] = ‘0’)
# Now we call binary(0); since (n<1) we print arr (0 is printed)
# The call returns to arr[n-1] = ‘1’ arr[1-1] is set as ‘1’ (arr[1-1] = arr[0] = ‘1’)
# Now we call binary(0); since (n<1) we print arr (1 is printed)
# Thus, we got 2 outputs as possible bits 0 and 1.

# Now let us suppose n = 2,
# The method is called as binary(2) arr[2-1] is set as ‘0’ (arr[2-1] = arr[1] = ‘0’)
#Now we call binary(1); From the above explanation we know that binary(1) produces an output of 0 and 1
# for arr[0]. Here arr[1] is set as 0. So we get the 2 outputs (00 and 01).
# The function returns to arr[n-1] = ‘1’ arr[2-1] is set as 1 (arr[2-1] = arr[1] = ‘1’)
# Again we call binary(1); This time arr[1] is set as ‘1’ and thus we get 2 more outputs (10 and 11).
#We have a total of 4 outputs on screen..(00, 01, 10, 11) These are all the strings of 2 bits.
class GenerateAllStringsOfNBits():
    def __init__(self, n):
        self.a = [0] * n
    def binary(self, n):
        if n < 1:
            print(''.join([str(i) for i in self.a]))
        else:
            self.a[n-1] = 0
            self.binary(n-1)
            self.a[n-1] = 1
            self.binary(n-1)

obj = GenerateAllStringsOfNBits(2)
obj.binary(2)


    
