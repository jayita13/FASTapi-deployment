from pydantic import BaseModel
# 2. Class which describes Diabetes measurements
class Diabetes(BaseModel):
    Pregnancies : float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float