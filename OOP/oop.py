# Python Object-Oriented Programming

class Employee:

    # class variable, can be accessed by all instances of the class
    num_of_employees = 0
    raise_amount = 1.05 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@company.com'
        self.pay = pay
        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # use self.raise_amount because it can be overridden by instance

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        Employee.num_of_employees += 1
        return cls(first, last, int(pay)) # return an instance of the class

    # static method: does not take self or cls as the first argument, 
    # they are utility functions that do not access or modify class or instance state
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Call the class method to set the raise amount for all employees
Employee.set_raise_amount(1.06)

emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

print(Employee.num_of_employees)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())

Employee.fullname(emp_1) # also an approach to call the method

emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)
# print(Employee.__dict__) # class variables are stored in the class __dict__ attribute

# emp_str_1 = 'John-Doe-50000'
# emp_str_2 = 'Jane-Smith-60000'
# emp_str_3 = 'Jim-Brown-70000'

# emp_1 = Employee.from_string(emp_str_1)
# emp_2 = Employee.from_string(emp_str_2)
# emp_3 = Employee.from_string(emp_str_3)

# print(emp_1.email)

import datetime
my_date = datetime.date(2024, 10, 17)
print(Employee.is_workday(my_date))
