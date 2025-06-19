class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property  # methods start acting like an attribute
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter  # decorator
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100


emp = Employee(50000, 10)
print(emp.salaryAfterIncrement)      # Output: 55000.0

emp.salaryAfterIncrement = 60000
print(emp.increment)                # Output: 20.0
