# Take marks input for 3 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Assume total marks for each subject is 100
total_marks = 300
obtained_marks = sub1 + sub2 + sub3
percentage = (obtained_marks / total_marks) * 100

# Check pass/fail conditions
if (sub1 >= 33 and sub2 >= 33 and sub3 >= 33) and (percentage >= 40):
    print("Congratulations! You have passed.")
else:
    print("Sorry, you have failed.")

# Optionally, print the total and percentage
print(f"Total Marks: {obtained_marks}/300")
print(f"Percentage: {percentage:.2f}%")
