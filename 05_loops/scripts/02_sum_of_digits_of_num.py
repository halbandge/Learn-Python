number = int(input("Enter a number:"))
number_copy = number

sum = 0
while number != 0:
    last_digit = number % 10
    number = number // 10
    sum += last_digit

print("Sum of Digits for", number_copy, "is", sum)