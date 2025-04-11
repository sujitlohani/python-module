class Employee:
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary

    def display_info (self):
        print (f"Employee Name: {self.name}")
        print (f"Employee Salary: {self.salary}")

class Manager (Employee):
    def __init__ (self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display_info (self):
        print (f"Manager Name: {self.name}")
        print (f"Manager Salary: {self.salary}")
        print (f"Manager team size: {self.team_size}")

    def bonus(self):
        bonus_amount = 0.10 * self.salary
        return (self.salary + bonus_amount)
    

def main():
    employee1 = Employee("Sajjan", 50000)
    employee2  =Employee("Anush", 60000)

    manager1 = Manager ("Sujit", 90000, 10)

    employee1.display_info()
    employee2.display_info()
    manager1.display_info()

    print(f"Bonus: {manager1.bonus()}")  




main()