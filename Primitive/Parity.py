# Parity: if number of 1 in a binary number is even
# parity is zero if odd parity is 1
# 2(10) parity is 1
# 3(11) parity is 0
#Brute force
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x>>= 1
    return result

print(parity(3))
