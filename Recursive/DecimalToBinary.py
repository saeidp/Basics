# recursive to print binaries
def decimalToBinary(n):
    if n > 1:
        decimalToBinary(n // 2 )
    print(n % 2,  end=" ")

#---------------------------------------------------------------------

# Simple conversion to binary
def decimalToBinary2(n):
    bin = ""
    while n > 1:
        bin = str(n % 2) + " " + bin
        n //= 2
    bin = str(n % 2) +  " " + bin
    return bin

result = decimalToBinary2(5)
print(result)
decimalToBinary(5)