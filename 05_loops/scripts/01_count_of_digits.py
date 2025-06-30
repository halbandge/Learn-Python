number = int(input("Enter a number:"))
number_copy = number

count = 0
while number != 0:
    number = number // 10
    count += 1

print("Count of Digits for", number_copy, "is", count)