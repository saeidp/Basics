# Write a program that outputs the string representation of
# numbers from 1 to n. But for multiples of three it should
# output “Fizz” instead of the number and for the multiples 
# of five output “Buzz”. For numbers which are multiples of 
# both three and five output “FizzBuzz”.
def int_to_fizzbuzz(i):
    entry = ''
    if i%3 == 0:
        entry += "fizz"
    if i%5 == 0:
        entry += "buzz"
    if i%3 != 0 and i%5 != 0:
        entry = i
    return entry

n = 15
fizzbuzz = [int_to_fizzbuzz(i) for i in range(1, n + 1)]
print(fizzbuzz)


# another version
def getFizzBuzz(n):
    fizz = 0
    buzz = 0
    result = []
    for i in range (1, n + 1):
        fizz += 1
        buzz += 1
        if fizz == 3 and buzz == 5:
            result.append("fizzBuzz")
            fizz = 0
            buzz = 0
        elif fizz == 3:
            result.append("fizz")
            fizz = 0
        elif buzz == 5:
            result.append("buzz")
            buzz = 0
        else:
            result.append(i)
    return result
        
print(getFizzBuzz(15))


        


