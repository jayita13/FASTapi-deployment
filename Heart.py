from pydantic import BaseModel

# Class which describes Diabetes measurements
class heart(BaseModel):
    Age: int
    Sex: int
    Chest_Pain_Type: int
    Resting_Blood_Pressure: float
    Serum_Cholestoral: float
    Fasting_Blood_Sugar: float
    Resting_Electrocardiographic_Results: int
    Maximum_Heart_Rate_Achieved: int
    Exercise_Induced_Angina: float
    Oldpeak: float
    Slope: float
    Number_Of_Major_Vessels: float
    Thal: int