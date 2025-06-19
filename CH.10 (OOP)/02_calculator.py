import math


class Calculator:
    def square(self, num):
        return num ** 2

    def cube(self, num):
        return num ** 3

    def sq_root(self, num):
        return math.sqrt(num)


cal = Calculator()
a = int(input("Enter a number: "))

print(f"The square of {a} is: {cal.square(a)}")
print(f"The cube of {a} is: {cal.cube(a)}")
print(f"The sq_root of {a} is: {cal.sq_root(a):.2f}")
