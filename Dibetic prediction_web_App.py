# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:01:32 2024

@author: HP
"""

import numpy as np
import pickle 
import streamlit as st

loaded_model=pickle.load(open('D:/Data Files Copy/Dibetic prediction model/trained_model.sav','rb'))
# CREATING A FUNCTION
def diabetic_prediction(input_data):
    
    #CHANGE THE INPUT DATA INTO ARRAY AND ITS IN TUPLE RIGHT NOW
    input_data_numpy=np.asarray(input_data)
    #RESHAPE THE NUMPY ARRAY AS WE ARE PREDICTION ONLY ONE DATA POINT
    reshaped_data=input_data_numpy.reshape(1,-1)
    prediction=loaded_model.predict(reshaped_data)
    print(prediction)
    if(prediction[0]==1):
      return "The patient is diabitic, we are srr.."
    else:
      return "Take a chill pill he is ok"
  
def main():
 #GIVING THE TITLE
    st.title("Diabetic Prediction App")
  #GETTING THE INPUT DATA FROM THE USER
    Pregnancies=st.text_input("Number of pregencies:")
    Glucose=st.text_input("Glucose:")
    BloodPressure=st.text_input("BloodPressure:")
    SkinThickness=st.text_input("SkinThickness:")
    Insulin=st.text_input("Insulin:")
    BMI=st.text_input("BMI:")
    DiabetesPedigreeFunction=st.text_input("DiabetesPedigreeFunction:")
    Age=st.text_input("Age:")
    
    #CODE FOR PREDICTION
    diagnosis=""
    
    #CREATING A BUTTON
    if st.button("Test Result"):
        diagnosis = diabetic_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)            
        
        
if __name__=='__main__':
    main()     