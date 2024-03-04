import streamlit as st
import random


# Title
st.title("RPA Demo")
st.session_state["user_input"] = st.text_input(label="Account number")
#st.session_state["outresult"]=""

###policy_check=""
def getQualityCheck(account_number):
    r = random.uniform(0, 1)
    #print("r: ", r)
    if r < 0.5:
        policy_check = account_number + ",3011"
    else:
        policy_check = account_number + ","
    
    st.session_state["outresult"]=policy_check

# Header
#st.header("Account Number") 
 
#number = st.number_input('Account number',format="%d")
#st.write('The account number is ', number)

###account_number = st.text_input("Account number")
#r = random.uniform(0, 1)
#if r < 0.5:
#    policy_check = account_number + ",3011"
#else:
#    policy_check = account_number + ","
st.button("Go", on_click=getQualityCheck, args=(st.session_state["user_input"],))

#st.button("Go", on_click=getQualityCheck())
st.write("The account number is: ", st.session_state["outresult"])