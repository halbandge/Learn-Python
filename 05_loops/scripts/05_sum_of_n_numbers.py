number = int(input("Enter the n'th number:"))

i = 1
sum = 0
while i <= number:
    sum += i
    i += 1

print("Sum of 1 to", number, "is", sum)