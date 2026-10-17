from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import List, Dict

# model_validator is a decorator that help us to right validation logic for the entire model.
class Patient(BaseModel):

    name: str
    age: int
    weight: float
    email: EmailStr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if isinstance(self.contact_details, dict) and isinstance(self.age, int):
            if self.age > 60 and 'emergency' not in self.contact_details:
                raise ValueError("Emergency contact is required for patients above 60 years old")
        return self

def update_patient_data(patient: Patient):
    print(f"Patient data updated: Name - {patient.name}, Age - {patient.age}")

patient_info = {'name': 'John Doe', 'age': 65, 'weight': 70.5, 'email': 'john.doe@icici.com', 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'emergency': '123-456-7890'}}
update_patient_data(Patient(**patient_info)) 
