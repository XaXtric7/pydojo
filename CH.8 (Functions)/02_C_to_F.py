def temp_con(C):
    F = (C * (9/5)) + 32
    return F


a = float(input("Enter the temperature in (C): "))
b = temp_con(a)

print(f"The temperature in (F): {b}")
