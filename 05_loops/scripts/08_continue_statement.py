i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue # divisble by 3 would not get printed
    print(i)