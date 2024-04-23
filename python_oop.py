class Employee:
    raise_amount = 1.04 #class variables
    num_emp = 0

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

emp1 = Employee("John", "Doe", 50000)
emp2 = Employee("Jane", "Doe", 60000)

emp1.raise_amount()
emp2.raise_amount()

print(emp1.pay)
print(emp2.pay)