username = input("Enter your username: ")
length = len(username)
if (length > 10):
    print("Username contains more than 10 characters.")
elif (length == 10):
    print("Username contains 10 characters.")
else:
    print("Username contains less than 10 characters.")
