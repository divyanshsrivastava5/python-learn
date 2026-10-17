from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict

# field_validator is a decorator that help us to right validation logic for single field.
class Patient(BaseModel):

    name: str
    age: int
    weight: float
    email: EmailStr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['icici.com', 'hdfc.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return value

    @field_validator('name')
    @classmethod
    def name_transform(cls, value):
        return value.upper()

    # mode -> before: validate before type coercion, after: validate after type coercion, plain: validate without type coercion
    @field_validator('age', mode='before')
    @classmethod
    def age_validator(cls, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        return value

def update_patient_data(patient: Patient):
    print(f"Patient data updated: Name - {patient.name}, Age - {patient.age}")

patient_info = {'name': 'John Doe', 'age': 30, 'weight': 70.5, 'email': 'john.doe@icici.com', 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890', 'email': 'john.doe@icici.com'}}
update_patient_data(Patient(**patient_info)) 
