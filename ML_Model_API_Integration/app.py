import uvicorn
from fastapi import FastAPI
from RoomDetails import RoomOccupancy
import numpy as np
import pickle
import pandas as pd


# Creating the app object using Fast API class
app = FastAPI()
pickle_in = open("room_occupancy_model_01.pkl","rb")
classifier=pickle.load(pickle_in)

# A welcome message to display at the root page
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# return the name parameter of the name specified
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome to the Room Occupancy Machine Learning Model...': f'{name}'}

# Temperature
# Humidity
# Light
# CO2
# HumidityRatio

@app.post('/predict')
def predict_occupancy(data:RoomOccupancy):
    data = data.dict()
    temperature=data['Temperature']
    humidity=data['Humidity']
    light=data['Light']
    co2=data['CO2']
    humidityratio=data['HumidityRatio']

    prediction = classifier.predict([[temperature,humidity,light,co2, humidityratio]])
    if(prediction[0]>0.5):
        prediction="Room occupany is available."
    else:
        prediction="Room Occupancy is not available at the moment."
    return {
        'prediction': prediction
    }

# running the API interface with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)