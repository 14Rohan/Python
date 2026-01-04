num = int(input("Enter a number: "))
if num > 1:  
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is NOT a prime number.")
            print(f"(It is divisible by {i})")
            break
    else:
        print(f"{num} is a PRIME number.")
else:
    print(f"{num} is NOT a prime number.")