s1 = set()
for i in range(7):
    a = input("Enter a number or str: ")
    if a.isdigit():
        s1.add(int(a))  # Convert to int
    else:
        s1.add(a)       # Keep as string
print(f"The set: {s1}")
