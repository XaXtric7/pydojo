from functools import reduce
# Map Example

l = [1, 2, 3, 4, 5]


def square(x): return x*x


# for i in l:
#     print(square(i), end=" ")

sqlist = map(square, l)
print(list(sqlist))

# Filter Example


def even(n):
    if (n % 2 == 0):
        return True
    return False


onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Example


def sum(a, b):
    return a + b


def mul(x, y): return x*y


print(reduce(sum, l))
print(reduce(mul, l))
