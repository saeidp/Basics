def genFib():
    fibn_1 = 1 # fib(n-1)
    fibn_2 = 0 # fib(n-2)

    while True:
        fibn = fibn_1 + fibn_2
        yield fibn
        fibn_2 = fibn_1
        fibn_1=fibn

fib = genFib()
print(0,1, end=" ")
for i in range(5):
    print(fib.__next__(), end=" ") # 1 2 3 5 8
