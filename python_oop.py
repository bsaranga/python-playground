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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True