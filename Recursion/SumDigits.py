#Given an integer, create a function which returns the
# sum of all the individual digits in that integer
def sum_digits(n):
    # Base case
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sum_digits(n// 10)

print(sum_digits(234))