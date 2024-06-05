# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:20:59 2024

@author: 91827
"""
import numpy as np
import pickle 
import streamlit as st


#loading the saved model
loaded_model =pickle.load(open('C:\\Users\\91827\\OneDrive\\Pictures\\MCA_Notes\\Projects\\trained_model.sav', 'rb'))

#creating a function for prediction

def weather_prediction(input_data):
    #input_data = [[25,1016,56,44,2.85]]
    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    ot = loaded_model.predict(input_data_reshaped)[0]
    print("The value of the ot:", ot)


    if ot == 0:
        return "The weather is: Broken Clouds"
    elif ot == 1:
        return "The weather is: Clear Sky"
    elif ot == 2:
        return "The weather is: Few Clouds"
    elif ot == 3: 
        return "The weather is: Heavy Rain"
    elif ot == 4: 
        return "The weather is: Light Rain"
    elif ot == 5: 
        return "The weather is: Light Snow"
    elif ot == 6: 
        return "The weather is: Moderate Rain"
    elif ot == 7: 
        return "The weather is: Overcast Clouds"
    elif ot == 8: 
        return "The weather is: Scattere Clouds"
    elif ot == 9: 
        return "The weather is: Snow"
    else:
        return "The weather is: Sunny"

def main():
    
    
    st.title('Weather and Climate risk Prediction web app ')
    
    #getting the input data from the user
        
    temp = st.number_input('Temperature (°C):', min_value=-15.00, max_value=50.00, step=1., format="%.2f")
    pressure = st.number_input('Pressure (mbar):', min_value=500, max_value=1500, step=1)
    humidity = st.number_input('Humidity (%):', min_value=0, max_value=100, step=1)
    clouds = st.number_input('Chance of (%):', min_value=0, max_value=100, step=1)
    wind_speed = st.number_input('Wind Speed (km/h):', min_value=0.00, max_value=15.00, step=1., format="%.2f")
    
    
    #code for prediction
    prediction = ' '
    
    if st.button('Predict'):
        prediction = weather_prediction([temp,pressure,humidity,clouds,wind_speed])
        
        
    st.success(prediction)
    
if __name__ == '__main__':
    main()
    
    
    
    
    