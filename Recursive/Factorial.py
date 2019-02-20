# Memoeization is just used if we calculate the values
# again for the steps after the first one like 10 and 20
memo = {}
def factorial(n):
    if n <2:
        return 1
    if not n in memo:
        memo[n] = n * factorial(n - 1)
    return memo[n]

print(factorial(10))
print(factorial(20))
