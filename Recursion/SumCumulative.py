#Write a recursive function which takes an integer
#  and computes the cumulative sum of 0 to that
# integer
#For example, if n=4 , return 4+3+2+1+0,
# which is 10
def rec_sum(n):
    # Base Case
    if n == 0:
        return 0
    # Recursion
    else:
        return n + rec_sum(n-1)

print(rec_sum(4))