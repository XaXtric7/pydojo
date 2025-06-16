def len_con(x):
    cm = x * 2.54
    return cm


a = float(input("Enter the length in inches: "))
b = len_con(a)

print(f"The length in (cm): {b}cm")
