# Given weights and values of n items, put these items in a knapsack of capacity W
# to get the maximum total value in the knapsack. In other words, given two integer
# arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated
# with n items respectively. Also given an integer W which represents knapsack capacity,
# find out the maximum value subset of val[] such that sum of the weights of this subset
# is smaller than or equal to W. You cannot break an item, either pick the complete item,
# or don’t pick it (0-1 property).

# Naive: Returns the maximum value that can be put in a knapsack of # capacity W 
# here it computes the same subproblems again and again
def knapSackNaive(W , wt , val , n): 
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knapSackNaive(W , wt , val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSackNaive(W-wt[n-1] , wt , val , n-1), knapSackNaive(W , wt , val , n-1))

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSackNaive(W , wt , val , n)) #220



# A Dynamic Programming based Python Program for 0-1 Knapsack problem 
# Returns the maximum value that can be put in a knapsack of capacity W 
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W , wt , val , n)) #220
