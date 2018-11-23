#A child is running up a staircase with n steps and
# can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the
# child can run up the stairs.

#Let's think about this with the following question: What is
# the very last step that is done?
# The very last hop the child makes-the one that lands her on
# the nth step-was either a 3-step hop, a 2-step hop, or a
# 1-step hop. How many ways then are there to get up to the
# nth step? We don't know yet, but we can relate it to some
# subproblems. If we thought about all of the paths to the
# nth step, we could just build them off the paths to the
# three previous steps. We can get up to the nth step by any
# of the following:

# Going to the (n - l)st step and hopping 1 step.
# Going to the (n - 2)nd step and hopping 2 steps.
# Going to the (n - 3)rd step and hopping 3 steps.
def countWays(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if memo[n] > -1:
        return memo[n]
    memo[n] = countWays(n-1, memo) + countWays(n-2, memo) + countWays(n-3, memo)
    return memo[n]

n = 3
memo = [-1] * (n + 1)
ways = countWays(n, memo)
print(ways) #4

n = 4
memo = [-1] * (n + 1)
ways = countWays(n, memo)
print(ways) #7


