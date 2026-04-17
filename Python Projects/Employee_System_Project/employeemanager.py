from employee import Employee

class EmployeesManager:
    def __init__(self):
        self.employees = []

    # Add employee
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} added successfully.")

    # List all employees
    def list_employees(self):
        if not self.employees:
            print("No employees found.")
            return

        print("\nEmployee List:")
        for emp in self.employees:
            print(emp)

    # Delete employees by age range
    def delete_by_age_range(self, min_age, max_age):
        original_count = len(self.employees)

        self.employees = [
            emp for emp in self.employees
            if not (min_age <= emp.age <= max_age)
        ]

        print(f"Deleted {original_count - len(self.employees)} employee(s).")

    # Find employee by name
    def find_employee(self, name):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                return emp
        return None

    # Update salary by name
    def update_salary(self, name, new_salary):
        emp = self.find_employee(name)
        if emp:
            emp.salary = new_salary
            print(f"{name}'s salary updated to ₹{new_salary}")
        else:
            print("Employee not found.")