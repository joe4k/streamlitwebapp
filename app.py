import streamlit as st
import random


# Title
st.title("RPA Demo")

def getRandom():
    r = random.uniform(0, 1)
    if r < 0.5:
        return 0
    else:
        return 1

# Header
#st.header("Account Number") 
 
#number = st.number_input('Account number',format="%d")
#st.write('The account number is ', number)

account_number = st.text_input("Account number")
r = random.uniform(0, 1)
if r < 0.5:
    policy_check = account_number + ",3011"
else:
    policy_check = account_number + ","
st.write("The account number is: ", policy_check)