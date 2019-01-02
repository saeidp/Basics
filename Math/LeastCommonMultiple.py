# The least common multiple of two positive integers a and b is the least
# positive integer m that is divisible by both a and b.
# Input:6 8
# Output: 24
# Explanation: Among all the positive integers that are divisible by both
# 6 and 8 (e.g., 48, 480, 24), 24 is the smallest one.
# using the following formula: LCM(a,b) * GCD(a,b) = a * b.
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    aPrime = a % b
    return greatest_common_divisor(b, aPrime)

def least_common_multiple(a, b):
    gcd = greatest_common_divisor(a,b)
    return (a * b) / gcd


d = least_common_multiple(4, 6)
print(d) #12

