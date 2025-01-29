import pickle
import streamlit as st
from os import path
import numpy as np

st.title("Credit Card Fraud Detection App")

filename="random.pkl"
with open(path.join(filename),'rb') as f:
    random = pickle.load(f)
    
V1 = st.number_input("Enter the 1st transaction id",key="input_1")
V2 = st.number_input("Enter the 2nd transaction id",key="input_2") 
V3 = st.number_input("Enter the 3rd transaction id",key="input_3") 
V4 = st.number_input("Enter the 4th transaction id",key="input_4")
V5 = st.number_input("Enter the 5th transaction id",key="input_5") 
V6 = st.number_input("Enter the 6th transaction id",key="input_6") 
V7 = st.number_input("Enter the 7th transaction id",key="input_7") 
V8 = st.number_input("Enter the 8th transaction id",key="input_8") 
V9 = st.number_input("Enter the 9th transaction id",key="input_9") 
V10= st.number_input("Enter the 10th transaction id",key="input_10") 
V11= st.number_input("Enter the 11th transaction id",key="input_11") 
V12= st.number_input("Enter the 12th transaction id",key="input_12") 
V13= st.number_input("Enter the 13th transaction id",key="input_13") 
V14= st.number_input("Enter the 14th transaction id",key="input_14") 
V15= st.number_input("Enter the 15th transaction id",key="input_15") 
V16= st.number_input("Enter the 16th transaction id",key="input_16") 
V17= st.number_input("Enter the 17th transaction id",key="input_17") 
V18= st.number_input("Enter the 18th transaction id",key="input_18") 
V19= st.number_input("Enter the 19th transaction id",key="input_19") 
V20= st.number_input("Enter the 20th transaction id",key="input_20") 
V21= st.number_input("Enter the 21th transaction id",key="input_21") 
V22= st.number_input("Enter the 22nd transaction id",key="input_22") 
V23= st.number_input("Enter the 23rd transaction id",key="input_23") 
V24= st.number_input("Enter the 24th transaction id",key="input_24") 
V25= st.number_input("Enter the 25th transaction id",key="input_25")
V26= st.number_input("Enter the 26th transaction id",key="input_26")  
V27= st.number_input("Enter the 27th transaction id",key="input_27")  
V28= st.number_input("Enter the 28th transaction id",key="input_28")  
V29= st.number_input("Enter the 29th transaction id",key="input_29")  
V30= st.number_input("Enter the 30th transaction id",key="input_30")  
   


if st.button("Detect"):
    pred = random.predict(np.array([[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,V29,V30]]))
    st.write("The transaction is :",pred[0])
