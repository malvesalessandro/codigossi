num = input("digite um numero?")
while num > 1:
    if num % 3 == 0:
        num = num/3
        print (num)
    else:
        if num % 3 == 1:
            num = num - 1
        elif num % 3 == 2:
            num = num + 1
