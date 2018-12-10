# Given an array of size n, remove all even integers from it.
# Sample Input arr = [1,2,4,5,10,6,3]
# Sample Output arr = [1,5,3]
def removeEven(arr):
    return [i for i in arr if i %2 !=0]

print(removeEven([1,2,4, 5, 10, 6, 3])) # [1, 5, 3]
