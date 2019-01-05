# The simple and naive solution is to have three nested loops to iterate over
# all unordered triples and see if their sum is equal to the given integer or
# not. Although this works, it is not efficient
# o(n^3), o(1)
def find_sum_of_three_v1(arr, required_sum):
    for i in range(0, len(arr) -2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if(i != j and j !=k and k != i):
                    sum = arr[i] + arr[j] + arr[k]
                    if(sum == required_sum):
                        return True
    return False

print(find_sum_of_three_v1([1,2,3,4], 6))

# To understand this solution better, we recommend taking a look at "Sum of Two
# Values".In this solution, we first sort the array. Then we fix one element
# 'e', and try to find a pair (a, b) in the remaining array such that
# required_sum - e = a + b.
# O(n^2), O(1)
def find_sum_of_two(A, val, start_index):
    i = start_index
    j = len(A) - 1
    while(i < j):
        s = A[i] + A[j]
        if(s == val):
            return True
        if(s < val):
            i += 1
        else:
            j -=1
    return False

def find_sum_of_three_v3(arr, required_sum):
    arr.sort()
    for i in range(0, len(arr) - 2):
        remaininig_sum = required_sum - arr[i]
        if(find_sum_of_two(arr, remaininig_sum, i+1)):
            return True
    return False

print(find_sum_of_three_v3([1,2,3,4], 6))
