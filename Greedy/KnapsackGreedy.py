# Given weights and values of n items, put these items in a knapsack of capacity W
# to get the maximum total value in the knapsack. In other words, given two integer
# arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated
# with n items respectively. Also given an integer W which represents knapsack capacity,
# find out the maximum value subset of val[] such that sum of the weights of this subset
# is smaller than or equal to W. You cannot break an item, either pick the complete item,
# or don’t pick it (0-1 property).

# This implemetation is in StackExchange as follows:
#  https://codereview.stackexchange.com/questions/150677/knapsack-greedy-algorithm-in-python
def get_optimal_value(capacity, weights, values):
    value = 0.
    valuePerWeight = valuePerWeight = sorted([[v / w, w] for v,w in zip(values,weights)], reverse=True)
    while capacity > 0 and valuePerWeight:
        maxi = 0
        idx = None
        for i,item in enumerate(valuePerWeight):
            if item [1] > 0 and maxi < item [0]:
                maxi = item [0]
                idx = i

        if idx is None:
            return 0.

        v = valuePerWeight[idx][0]
        w = valuePerWeight[idx][1]

        if w <= capacity:
            value += v*w
            capacity -= w
        else:
            if w > 0:
                value += capacity * v
                return value
        valuePerWeight.pop(idx)

    return value

n = 3
capacity = 50
values = [60, 100, 120]
weights = [20, 50, 30]
opt_value = get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value)) # print 180.0000000000