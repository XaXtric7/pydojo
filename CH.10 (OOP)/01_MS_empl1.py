class Programmer:
    def __init__(self):
        self.database = {}

    def addInfo(self):
        name = input("Enter the name of the employee: ").strip()
        position = input("Enter the position of the employee: ").strip()
        salary = input("Enter the salary of the employee: ").strip()

        self.database[name] = {
            'position': position,
            'salary': salary
        }
        print(f"✅ Employee '{name}' added successfully!\n")

    def showInfo(self, name):
        if name in self.database:
            print(f"\n📋 Info of {name}:")
            print(f"Position: {self.database[name]['position']}")
            print(f"Salary: {self.database[name]['salary']}")
        else:
            print(f"\n❌ Employee '{name}' does not exist in the records.\n")


# ---------- Usage Example ----------
company = Programmer()

while True:
    print("\n1. Add Employee Info")
    print("2. Show Employee Info")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        company.addInfo()
    elif choice == '2':
        name_to_find = input(
            "Enter the name of the employee to search: ").strip()
        company.showInfo(name_to_find)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("⚠️ Invalid choice. Try again.")
