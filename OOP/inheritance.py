'''
class Developer(Employee):
    Method resolution order:
    1. Developer
    2. Employee
    3. built-in 'object' class (Base class for all classes in Python)
'''

class Employee:
    raise_amount = 1.04 # class variable
 
    def __init__(self, first, last, pay):
         self.first = first
         self.last = last
         self.pay = pay
         self.email = f'{first.lower()}.{last.lower()}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10 # class variable

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # call the parent class constructor
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
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
            print('-->', emp.fullname())

dev_1 = Developer('John', 'Doe', 50000, 'Python')
dev_2 = Developer('Jane', 'Smith', 60000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)
print(dev_2.email)
print(dev_2.prog_lang)

manager_1 = Manager('Sue', 'Jones', 90000, [dev_1])
print(manager_1.email)
manager_1.print_employees()

manager_2 = Manager('Tom', 'Brown', 80000)
manager_2.add_employee(dev_2)
print(manager_2.email)
manager_2.print_employees()

print(isinstance(manager_1, Manager)) # True
print(isinstance(manager_1, Employee)) # True
print(issubclass(Manager, Employee)) # True