class Employee:
    raise_amount = 1.04 #class variables
    num_emp = 0

    def __add__(self, other):
        return self.pay + other.pay

    def __repr__(self) -> str:
        return f"Employee({self.firstName}, {self.lastName}, {self.pay})"
    
    def __str__(self) -> str:
        return f"{self.fullName()} - {self.email}"

    def __init__(self, firstName, lastName, pay) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f"{firstName}.{lastName}@company.com"
        Employee.num_emp += 1

    def fullName(self):
        return f"{self.firstName} {self.lastName}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, firstName, lastName, pay, prog_lang) -> None:
        super().__init__(firstName, lastName, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, firstName, lastName, pay, employees=None) -> None:
        super().__init__(firstName, lastName, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print("-->", emp.fullName())


emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Jane', 'Doe', 60000)

print(emp1 + emp2)