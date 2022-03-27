# import libraries
import uvicorn
from fastapi import FastAPI
from Diabetes import Diabetes
import joblib

# Create the app object
app = FastAPI()
# model = open("random_forest.joblib", "r")
classifier = joblib.load("random_forest.joblib", mmap_mode="r+")

# Index route, opens http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello there'}

# route with a single parameter returns parameter within a message
@app.get('/Welcome')
def get_name(name: str):
    return('Welcome to my webpage:' f'{name}')

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Diabetes with the confidence
@app.post('/predict')
def predict_diabetes(data: Diabetes):
    data = data.dict()
    pregnancy = data['Pregnancies']
    glucose = data['Glucose']
    bloodpressure = data['BloodPressure']
    skinthickness = data['SkinThickness']
    insulin = data['Insulin']
    bmi = data['BMI']
    dpf = data['DiabetesPedigreeFunction']
    age = data['Age']
    prediction = classifier.predict([[pregnancy, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]])
    if(prediction[0]>0.5):
        prediction = "Not Diabetic"
    else:
        prediction = "Diabetic"
    return {
        'prediction': prediction
    }

# Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn main:app --reload
