#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data 
pickle_in = open('model.pkl', 'rb') 
model = pickle.load(pickle_in) 
  
def welcome(): 
    return 'welcome all'
  
# defining the function which will make the prediction using  
# the data which the user inputs 
def prediction(Annual_Income, Monthly_Inhand_Salary, Num_Bank_Accounts,
       Num_Credit_Card, Interest_Rate, Num_of_Loan,
       Delay_from_due_date, Num_of_Delayed_Payment, Credit_Mix,
       Outstanding_Debt, Credit_History_Age, Monthly_Balance):   
   
    prediction = classifier.predict( 
        [[Annual_Income, Monthly_Inhand_Salary, Num_Bank_Accounts,
       Num_Credit_Card, Interest_Rate, Num_of_Loan,
       Delay_from_due_date, Num_of_Delayed_Payment, Credit_Mix,
       Outstanding_Debt, Credit_History_Age, Monthly_Balance]]) 
    print(prediction) 
    return prediction 
      
  
# this is the main function in which we define our webpage  
def main(): 
      # giving the webpage a title 
    st.title("Credit Score Classification Prediction") 
      
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding and the text to be displayed 
    html_temp = """ 
    <div style ="background-color:mistyrose;padding:8px"> 
    <h1 style ="color:black;text-align:center;">Credit Score Classifier ML App </h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
    
    Annual_Income = st.text_input('Annual Income') 
    Monthly_Inhand_Salary = st.text_input("Monthly Inhand Salary")
    Num_Bank_Accounts = st.text_input("Number of Bank Accounts")
    Num_Credit_Card = st.text_input("Number of Credit cards")
    Interest_Rate = st.text_input("Interest rate")
    Num_of_Loan = st.text_input("Number of Loans")
    Delay_from_due_date = st.text_input("Average number of days delayed by the person")
    Num_of_Delayed_Payment = st.text_input("Number of delayed payments")
    Credit_Mix = st.text_input("Credit Mix (Bad: 0, Standard: 1, Good: 2)")
    Outstanding_Debt = st.text_input("Outstanding Debt")
    Credit_History_Age = st.text_input("Credit History Age")
    Monthly_Balance = st.text_input("Monthly Balance")
    
    result ="" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if st.button("Predict"): 
        result = prediction(Annual_Income, Monthly_Inhand_Salary, Num_Bank_Accounts,
       Num_Credit_Card, Interest_Rate, Num_of_Loan,
       Delay_from_due_date, Num_of_Delayed_Payment, Credit_Mix,
       Outstanding_Debt, Credit_History_Age, Monthly_Balance) 
    st.success('The output is {}'.format(result)) 
     
if __name__=='__main__': 
    main() 


# In[ ]:





# In[ ]:




