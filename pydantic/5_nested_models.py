from pydantic import BaseModel

'''
useful as in:
    1. readability
    2. maintainability
    3. reusability
'''

class Address(BaseModel):
    city: str
    state: str
    pin_code: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address

address_dict = {'city' : 'Noida', 'state' : 'Uttar Pradesh', 'pin_code' : '201301'}
address = Address(**address_dict)

patient_dict = {'name' : 'John Doe', 'age' : 30, 'gender' : 'Male', 'address' : address_dict}
patient = Patient(**patient_dict)

print(patient)
print(patient.address.city)