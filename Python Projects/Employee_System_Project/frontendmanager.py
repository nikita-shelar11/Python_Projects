from employeemanager import EmployeesManager
from employee import Employee

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def run(self):
        while True:
            print("\n===== EMPLOYEE SYSTEM =====")
            print("1. Add Employee")
            print("2. List Employees")
            print("3. Delete by Age Range")
            print("4. Update Salary")
            print("5. Find Employee")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                salary = float(input("Enter salary: "))
                emp = Employee(name, age, salary)
                self.manager.add_employee(emp)

            elif choice == "2":
                self.manager.list_employees()

            elif choice == "3":
                min_age = int(input("Enter min age: "))
                max_age = int(input("Enter max age: "))
                self.manager.delete_by_age_range(min_age, max_age)

            elif choice == "4":
                name = input("Enter name: ")
                new_salary = float(input("Enter new salary: "))
                self.manager.update_salary(name, new_salary)

            elif choice == "5":
                name = input("Enter name: ")
                emp = self.manager.find_employee(name)
                if emp:
                    print(emp)
                else:
                    print("Employee not found.")

            elif choice == "6":
                print("Exiting system...")
                break

            else:
                print("Invalid choice!")