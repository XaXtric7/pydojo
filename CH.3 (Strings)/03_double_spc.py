string1 = input("Enter the string: ")
length = len(string1)

found = False
for i in range(length - 1):
    if string1[i] == " " and string1[i + 1] == " ":
        found = True
        break

if found:
    print("This string contains double spaces.")
else:
    print("This string doesn't contain double spaces.")
