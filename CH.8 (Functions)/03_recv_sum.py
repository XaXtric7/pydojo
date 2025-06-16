def sum_natural(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    return n + sum_natural(n - 1)


# Example usage
n = int(input("Enter a natural number: "))
if n >= 1:
    print(f"Sum of first {n} natural numbers is: {sum_natural(n)}")
else:
    print("Please enter a natural number greater than 0.")
