class Employee:

    def __init__(self, first, last):
         self.first = first
         self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    
emp_1 = Employee('John', 'Doe')
# emp_1.first = 'Jim' # change the first name of emp_1
# print(emp_1.first)
# print(emp_1.email) # email is not updated because it was set in the constructor and is not a property

print(emp_1.email)
print(emp_1.fullname) # used as a property, no need to call it as a method

emp_1.fullname = 'Jim Brown' # this will call the setter method for fullname and update first and last name
print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname # this will call the deleter method for fullname and set first and last name to None
