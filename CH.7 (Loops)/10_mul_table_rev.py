num = int(input("Enter a number: "))
print(f"The multiplication table of {num}")
for i in range(10, 0, -1):
    print(f"{num} * {i} = {num * i}")
