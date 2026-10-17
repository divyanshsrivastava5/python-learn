from pydantic import BaseModel

# used in exporting data to json or dict format

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

temp = patient.model_dump() # dict
print(type(temp))

temp_json = patient.model_dump_json() # str
print(type(temp_json))

print(patient.model_dump(include={'name', 'age'}, exclude_unset=True)) # dict