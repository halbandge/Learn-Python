number = int(input("Enter the number you want factorial of:"))

factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial of", number, "is", factorial)