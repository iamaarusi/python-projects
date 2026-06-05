num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

if num > 1:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
else:
    print("Not a Prime Number")