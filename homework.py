import json
import os

class Person:
    def __init__(self, name, age, designation, salary):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'designation': self.designation,
            'salary': self.salary
        }

class EmployeeManager:
    FILE_NAME = 'employees.json'

    def __init__(self):
        self.employees = self.load_employees()

    def load_employees(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        with open(self.FILE_NAME, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    def save_employees(self):
        with open(self.FILE_NAME, 'w') as file:
            json.dump(self.employees, file, indent=4)

    def create_employee(self):
        while True:
            try:
                name = input("Enter name: ").strip()
                age = int(input("Enter age: "))
                designation = input("Enter designation: ").strip()
                salary = float(input("Enter salary: "))

                person = Person(name, age, designation, salary)
                self.employees.append(person.to_dict())
                self.save_employees()

                cont = input("Do you want to add another employee? (yes/no): ").strip().lower()
                if cont == 'no':
                    break
            except ValueError:
                print("Invalid input. Please enter correct credentials.")
    
    def display_employees(self):
        if not self.employees:
            print("No employee records found.")
            return
        print("\n--- Employee Records ---")
        for emp in self.employees:
            print(f"Name: {emp['name']}, Age: {emp['age']}, Designation: {emp['designation']}, Salary: ₹{emp['salary']}")
        print()

    def raise_salary(self):
        name = input("Enter the name of the employee for salary hike: ").strip()
        found = False
        for emp in self.employees:
            if emp['name'].lower() == name.lower():
                try:
                    percent = float(input("Enter percentage hike (max 30%): "))
                    if percent < 0 or percent > 30:
                        raise ValueError("Percentage must be between 0 and 30.")
                    old_salary = emp['salary']
                    emp['salary'] += emp['salary'] * (percent / 100)
                    print(f"Salary updated: ₹{old_salary} → ₹{emp['salary']:.2f}")
                    found = True
                    self.save_employees()
                    break
                except ValueError as ve:
                    print(f"Error: {ve}")
        if not found:
            print("Employee not found.")

    def run(self):
        while True:
            print("\n--- MENU ---")
            print("1. Create Employee")
            print("2. Display Employees")
            print("3. Raise Salary")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_employee()
            elif choice == '2':
                self.display_employees()
            elif choice == '3':
                self.raise_salary()
            elif choice == '4':
                print("Thank you for using the application.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.run()
