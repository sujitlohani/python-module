class Employee:
    def __init__ (self, employee_id, salary):
        self.employee_id = employee_id
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    def display_info(self):
        print (f"Employee Name: {self.employee_id}")
        print (f"Employee Salary: {self.salary}")

class Manager (Employee):
    def __init__ (self, employee_id, salary, department):
        super().__init__(employee_id, salary)
        self.department = department

    def display_info (self):
        print (f"Manager Name: {self.employee_id}")
        print (f"Manager Salary: {self.salary}")
        print (f"Manager department: {self.department}")


class Developer (Employee):
    def __init__ (self, employee_id, salary,  programming_language):
        super().__init__(employee_id, salary)
        self.programming_language = programming_language

    def display_developer_info (self):
        print (f"Developer Name: {self.employee_id}")
        print (f"Developer Salary: {self.salary}")
        print (f"Developer programming language: {self.programming_language}")

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be a positive number!")

    def get_programming_language(self):
        return self.programming_language

    def set_programming_language(self, programming_language):
        self.programming_language = programming_language


def main():
    employee1 = Employee(101, 50000)
    manager1 = Manager(201, 90000, "HR")
    developer1 = Developer(301, 150000, "Python")

    employee1.display_info()
    manager1.display_info()
    developer1.display_info()

    print("\nUpdating Developer's salary...")
    developer1.set_salary(160000) 
    print(f"Updated Developer Salary: {developer1.get_salary()}")

    print("\nUpdating Developer's programming language...")
    developer1.set_programming_language("Java")
    print(f"Updated Developer Programming Language: {developer1.get_programming_language()}")

main()

    