number = int(input("Enter how many numbers you want to find maximum number among? "))

i = 1
max_number = None
while i <= number:
    new_num = int(input(f"Enter the {number} numbers:"))
    if max_number == None:
        max_number = new_num
    elif (new_num > max_number):
        max_number = new_num
    i += 1

print("Maximum number:", max_number)