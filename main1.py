import pickle
import streamlit as st
from os import path
import numpy as np

st.title("Credit Card Fraud Detection App")

filename="random.pkl"
with open(path.join(filename),'rb') as f:
    random = pickle.load(f)
    
V1 = st.number_input("Enter the transaction id")
V2 = st.number_input("Enter the transaction id") 
V3 = st.number_input("Enter the transaction id") 
V4 = st.number_input("Enter the transaction id")
V5 = st.number_input("Enter the transaction id") 
V6 = st.number_input("Enter the transaction id") 
V7 = st.number_input("Enter the transaction id") 
V8 = st.number_input("Enter the transaction id") 
V9 = st.number_input("Enter the transaction id") 
V10= st.number_input("Enter the transaction id") 
V11= st.number_input("Enter the transaction id") 
V12= st.number_input("Enter the transaction id") 
V13= st.number_input("Enter the transaction id") 
V14= st.number_input("Enter the transaction id") 
V15= st.number_input("Enter the transaction id") 
V16= st.number_input("Enter the transaction id") 
V17= st.number_input("Enter the transaction id") 
V18= st.number_input("Enter the transaction id") 
V19= st.number_input("Enter the transaction id") 
V20= st.number_input("Enter the transaction id") 
V21= st.number_input("Enter the transaction id") 
V22= st.number_input("Enter the transaction id") 
V23= st.number_input("Enter the transaction id") 
V24= st.number_input("Enter the transaction id") 
V25= st.number_input("Enter the transaction id")
V26= st.number_input("Enter the transaction id")  
V27= st.number_input("Enter the transaction id")  
V28= st.number_input("Enter the transaction id")  
V29= st.number_input("Enter the transaction id")  
V30= st.number_input("Enter the transaction id")  
   


if st.button("Detect"):
    pred = random.predict(np.array([[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,V29,V30]]))
    st.write("The transaction is :",pred[0])