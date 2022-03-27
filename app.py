# import libraries
import uvicorn
from fastapi import FastAPI
from Diabetes import Diabetes
from Heart import heart
import joblib

# Create the app object
app = FastAPI()

classifier_diabetes = joblib.load("models/random_forest_diabetes.joblib", mmap_mode="r+")
classifier_heart = joblib.load("models/random_forest_heart.joblib", mmap_mode="r+")

# Index route, opens http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Welcome to Disease Prediction'}

# route with a single parameter returns parameter within a message
@app.get('/Welcome')
def get_name(name: str):
    return('Welcome to my webpage:' f'{name}')

# Expose the prediction functionality, make a prediction from the passed
# JSON data and return the predicted Diabetes with the confidence
@app.post('/diabetes')
async def predict_diabetes(data: Diabetes):
    data = data.dict()
    pregnancy = data['Pregnancies']
    glucose = data['Glucose']
    bloodpressure = data['BloodPressure']
    skinthickness = data['SkinThickness']
    insulin = data['Insulin']
    bmi = data['BMI']
    dpf = data['DiabetesPedigreeFunction']
    age = data['Age']
    prediction = classifier_diabetes.predict([[pregnancy, glucose, bloodpressure, skinthickness,
                                               insulin, bmi, dpf, age]])
    if prediction[0] > 0.5:
        prediction = "Not Diabetic"
    else:
        prediction = "Diabetic"
    return {
        'prediction': prediction
    }

@app.post('/heart')
async def predict_heart(data: heart):
    data = data.dict()
    age = data['Age']
    sex = data['Sex']
    chest_pain_type = data['Chest_Pain_Type']
    resting_blood_pressure = data['Resting_Blood_Pressure']
    serum_cholestoral = data['Serum_Cholestoral']
    fasting_blood_sugar = data['Fasting_Blood_Sugar']
    resting_electrocardiographic_results = data['Resting_Electrocardiographic_Results']
    maximum_heart_rate_achieved = data['Maximum_Heart_Rate_Achieved']
    exercise_induced_angina = data['Exercise_Induced_Angina']
    oldpeak = data['Oldpeak']
    slope = data['Slope']
    no_of_major_vessels = data['Number_Of_Major_Vessels']
    thal = data['Thal']
    prediction = classifier_heart.predict([[age, sex, chest_pain_type, resting_blood_pressure, serum_cholestoral,
                                      fasting_blood_sugar, resting_electrocardiographic_results,
                                      maximum_heart_rate_achieved, exercise_induced_angina, oldpeak, slope,
                                      no_of_major_vessels, thal]])
    if(prediction[0]>0.5):
        prediction = "No Heart Disease"
    else:
        prediction = "Heart Disease"
    return {
        'prediction': prediction
    }

# Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn app:app --reload
