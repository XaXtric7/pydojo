def max_num(x, y, z):
    maxi = 0
    maxi = max(maxi, a)
    maxi = max(maxi, b)
    maxi = max(maxi, c)
    return maxi


a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

print(f"The max of those numbers is: {max_num(a, b, c)}")

# def max_num(*args):
#     return max(args)

# print(f"The max of those numbers is: {max_num(a, b, c)}")
