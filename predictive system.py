# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

#loading the saved model
loaded_model=pickle.load(open('C:/Users/hp/thyroid detection/trained_thyroid_model.sav','rb'))


input_data=a_data.reshape(1,-1)

prediction=loaded_model.predict(input_data)
print(prediction)

if(prediction[0]==0):
    print('The person has no thyroid')
elif(prediction[0]==1):
    print('The person has Compensated Hypothyroid')
elif(prediction[0]==2):
    print('The person has Primary Hypothyroid')
else:
    print('The person has Secondary Hypothyroid')
 