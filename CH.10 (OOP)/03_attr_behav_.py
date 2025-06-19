class Sample:
    a = 5  # Class attribute


obj = Sample()
obj.a = 0  # Changes or creates an instance attribute, not the class attribute

print(Sample.a)  # Still 5
print(obj.a)     # 0
