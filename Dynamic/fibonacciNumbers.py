#The following code prints all Fibonacci numbers
# from 0 to n. using memoization O(N)
def fib(n, memo):
    if n <= 0:
        return 0
    elif n==1:
        return 1
    elif memo[n] > 0:
         return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


memo=[0] * 7
for i in range(7):
    print(fib(i, memo), end=" ") # 0,1,1,2,3,5,8

