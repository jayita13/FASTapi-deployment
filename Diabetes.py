from pydantic import BaseModel

# Class which describes Diabetes measurements
class Diabetes(BaseModel):
    Pregnancies : int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
