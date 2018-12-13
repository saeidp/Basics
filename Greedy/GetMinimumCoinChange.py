# The goal in this problem is to find the minimum number of coins needed to change the input value
# (an integer) into coins with denominations 1, 5, and 10.
# input: 2
# Output: 2 = 1 + 1

# input: 28
# output: 10 + 10 + 5 + 1 + 1+ 1
# a simplified version
def GetChange(m):
    coin1 = 1
    coin5 = 5
    coin10 = 10

    coin10Num = m // coin10

    remainder10 = m % coin10
    remainder5 = remainder10 % coin5

    coin5Num = remainder10 // coin5
    coin1Num = remainder5 // coin1
 
    coinNumbers = coin10Num + coin5Num + coin1Num
    return coinNumbers

print(GetChange(2)) # 2
print(GetChange(28)) #6

# a generic version
def getChange2(m):
    coins= [10, 5, 1]
    min = 0
    i = 0
    while m >0:
        min += m // coins[i]
        m %= coins[i]
        i +=1
    return min

print(GetChange(2)) # 2
print(GetChange(28)) #6
