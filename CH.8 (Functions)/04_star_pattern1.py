def star(n):
    for i in range(n):
        print("*" * (n - i))


n = int(input("Enter the value of n: "))
star(n)
