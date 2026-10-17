'''
problems:
    1. type validation
    2. code duplication
    3. data validation
'''

# def update_patient_data(name: str, age: int):
#     if type(name) == str and type(age) == int:
#         print(f"Patient data updated: Name - {name}, Age - {age}")
#     else:
#         raise TypeError('Incorrect data type')



#---------------------------------------------------------
from pydantic import BaseModel,EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(min_length=1, max_length=50, json_schema_extra={'example': 'John Doe'}, description='Name of the patient')]
    email: EmailStr
    linkedIn: Optional[AnyUrl] = None
    age: int = Field(ge=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True, description='Weight of the patient in kg')]
    married: Annotated[bool, Field(default=False, description='Marital status of the patient')]
    allergies: Optional[List[str]] = Field(max_length=5)
    contact_details: Optional[Dict[str, str]] = None

patient_info = {'name': 'John Doe', 'email': 'john.doe@example.com', 'linkedIn': 'https://www.linkedin.com/in/johndoe', 'age': 30, 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890', 'email': 'john.doe@example.com'}}
patient_1 = Patient(**patient_info)

def insert_patient_data(patient: Patient):
    print(f"Patient data updated: Name - {patient.name}, Age - {patient.age}")

insert_patient_data(patient_1)

def update_patient_data(patient: Patient):
    print(f"Patient data updated: Name - {patient.name}, Age - {patient.age}")

