# The greatest common divisor GCD(a,b) of two non-negative integers a and b
# (which are not both equal to 0) is the greatest integer d that divides both
# a and b. Your goal in this problem is to implement the Euclidean algorithm
# for computing the greatest common divisor.
# for example 4,6 -> 2

# Naive
def gcd_naive(a,b):
    gcd = 1
    d = 2
    while d <= a and d <= b:
        if a % d == 0 and b % d == 0:
            gcd = d
        d += 1
    return gcd

gcd = gcd_naive(4, 6)
print(gcd) #2


# fast algorithm as it doesn't need to loop through all values untill reach a or b 
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    aPrime = a % b
    return greatest_common_divisor(b, aPrime)

gcd = greatest_common_divisor(4, 6)
print(gcd)#2