marks = []
st = 0
for i in range(6):
    st += 1
    a = int(input(f"Enter the marks of student {st}: "))
    marks.append(a)
marks.sort()
print(marks)