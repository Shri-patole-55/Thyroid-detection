# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:57:10 2023

@author: hp
"""

import numpy as np
import pickle 
import streamlit as st
import pandas as pd

#loading the saved model
loaded_model=pickle.load(open('C:/Users/hp/thyroid detection/trained_thyroid_model.sav','rb'))

#creating a function for prediction

def thyroid_prediction(input_data):
    
    input_data=np.asarray(input_data)
    
    input_data=input_data.reshape(1,-1)

    prediction=loaded_model.predict(input_data)
    print(prediction)

    if(prediction[0]==0):
        return 'The person has no thyroid'
    elif(prediction[0]==1):
        return 'The person has Compensated Hypothyroid'
    elif(prediction[0]==2):
        return 'The person has Primary Hypothyroid'
    else:
        return 'The person has Secondary Hypothyroid'

def main():
    #giving a title
    st.title('Thyroid Detection')
    
    #getting the input data from user
    age= st.slider("Age", 1, 100,1)
    gender= st.selectbox("Gender",options=['Male' , 'Female'])
    on_thyroxine= st.selectbox("On thyroxine?",options=['Yes','No'])
    query_on_thyroxine=st.selectbox("Query On thyroxine?",options=['Yes','No'])
    on_antithyroid_medication=st.selectbox("Antithyroid Medications?",options=['Yes','No'])
    sick=st.selectbox("feeling sick?",options=['Yes','No'])
    pregnant=st.selectbox("Pregnancy",options=['Yes','No'])
    thyroid_surgery=st.selectbox("Thyroid surgery History",options=['Yes','No'])
    I131_treatment=st.selectbox("On I131 Treatment",options=['Yes','No'])
    query_hypothyroid=st.selectbox("Query on Hypothyroid",options=['Yes','No'])
    query_hyperthyroid=st.selectbox("Query on Hyperthyroid",options=['Yes','No'])
    lithium=st.selectbox("Lithium Report",options=['Positive','Negative'])
    goitre=st.selectbox("Goitre",options=['Positive','Negative'])
    tumor=st.selectbox("Tumor",options=['Positive','Negative'])
    hypopituitary=st.selectbox("hypopituitary",options=['Positive','Negative'])
    psych=st.selectbox("psych",options=['Positive','Negative'])
    T3=st.number_input("T3 value ",step=1,format="%.2f")
    TT4=st.number_input("TT4 value",step=1,format="%.2f")
    T4U=st.number_input("T4U value",step=1,format="%.2f")
    FTI=st.number_input("FTI value",step=1,format="%.2f")
    
    gender = 1 if gender == 'Male' else 0
    on_thyroxine= 1 if on_thyroxine=='Yes' else 0
    query_on_thyroxine= 1 if query_on_thyroxine=='Yes' else 0
    on_antithyroid_medication=1 if on_antithyroid_medication=='yes' else 0
    sick= 1 if sick=='Yes' else 0
    pregnant= 1 if pregnant=='Yes' else 0
    thyroid_surgery= 1 if thyroid_surgery=='Yes' else 0
    I131_treatment= 1 if I131_treatment=='Yes' else 0
    query_hypothyroid= 1 if query_hypothyroid=='Yes' else 0
    query_hyperthyroid= 1 if query_hyperthyroid=='Yes' else 0
    lithium= 1 if lithium=='Positive' else 0
    goitre= 1 if goitre=='Positive' else 0
    tumor= 1 if tumor=='Positive' else 0
    hypopituitary= 1 if hypopituitary=='Positive' else 0
    psych= 1 if psych=='Positive' else 0
    
    #code for prediction
    diagnosis=''
    
    #creating a button for prediction
    if st.button('Predict the Result'):
        diagnosis = thyroid_prediction([age,gender,on_thyroxine,query_on_thyroxine,on_antithyroid_medication,sick,pregnant,thyroid_surgery,I131_treatment,query_hypothyroid,query_hyperthyroid,lithium,goitre,tumor,hypopituitary,psych,T3,TT4,T4U,FTI])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
    













