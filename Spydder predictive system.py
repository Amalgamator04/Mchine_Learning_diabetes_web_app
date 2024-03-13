import numpy as np
import pickle
#LOADING THE SAVED MODEL
loaded_model=pickle.load(open('D:/Data Files Copy/Dibetic prediction model/trained_model.sav','rb'))
input_data=(41,0,1,130,204,0,0,172,0,1.4,2,0,2)
#CHANGE THE INPUT DATA INTO ARRAY AND ITS IN TUPLE RIGHT NOW
input_data_numpy=np.asarray(input_data)
#RESHAPE THE NUMPY ARRAY AS WE ARE PREDICTION ONLY ONE DATA POINT
reshaped_data=input_data_numpy.reshape(1,-1)
prediction=loaded_model.predict(reshaped_data)
print(prediction)
if(prediction[0]==1):
  print ("The patient is diabitic, we are srr..")
else:
  print ("Take a chill pill he is ok")