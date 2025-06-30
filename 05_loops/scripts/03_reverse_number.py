number = int(input("Enter a number:"))
number_copy = number

reverse_number = ''
while number != 0:
    last_digit = number % 10
    number = number // 10
    reverse_number += str(last_digit)

print("Reverse of Digits for", number_copy, "is", reverse_number)