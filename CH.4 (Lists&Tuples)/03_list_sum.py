nums = []
sum = 0
for i in range(4):
    a = int(input("Enter the number: "))
    nums.append(a)
for i in nums:
    sum += i
print(f"The nums list is : {nums}")
print(f"The sum of the numbers is : {sum}")