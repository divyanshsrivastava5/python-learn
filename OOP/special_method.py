class Employee:

    raise_amount = 1.04 # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

'''
why it prints the __str__ method and not the __repr__ method? Because the print
function calls the __str__ method of the object, if it is defined. If __str__ is not defined, 
it will call __repr__. The __str__ method is meant to be a user-friendly representation of the
object, while __repr__ is meant to be an unambiguous representation of the object that can be 
used to recreate the object.
 '''
print(emp_1)  

# recreate the object from the __repr__ method
emp_3 = eval(repr(emp_1))
print(emp_3)  # Employee('John', 'Doe', 50000)

print(repr(emp_1))
print(str(emp_1))

print(1 + 2)
print(int.__add__(1, 2)) # this is how the + operator works, it calls the __add__ method of the int class
print(str.__add__('a', 'b')) # this is how the + operator works, it calls the __add__ method of the str class

print(emp_1 + emp_2) # this is how the + operator works, it calls the __add__ method of the Employee class

print(len('test'))
print(str.__len__('test')) # this is how the len function works, it calls the __len__ method of the str class

print(len(emp_1)) # this is how the len function works, it calls the __len__ method of the Employee class