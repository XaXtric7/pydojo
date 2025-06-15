a = input("Enter the data: ")
for i in a:
    if(a.isdigit()):
        a = int(a)
        break
    elif(i == "."):
        a = float(a)
        break
    else:
        a = str(a)
b = type(a)
print(a, "is of this type ->", b)