from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    height: float
    email: EmailStr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)

patient_info = {'name': 'John Doe', 'age': 30, 'weight': 70.5, 'height': 1.75, 'email': 'john.doe@icici.com', 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'emergency': '123-456-7890'}}
patient = Patient(**patient_info)
print(f"Patient BMI: {patient.bmi}")