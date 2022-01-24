"""

"""

__author__ = "sryborg44"
__copyright__ = "Copyright 2021, Susmit"
__status__ = "Dev"

##################################################
import os
import json
import traceback
import yaml
import shutil
import streamlit as st
from datetime import datetime

##################################################

########### Core Functions #######################
def calculate_exec_time(func):
    def func_wrapper(*args, **kwargs):
        func_name = func.__name__
        start = datetime.now()
        print("Function >> {} ".format(func_name))
        result = func(*args, **kwargs)
        print(
            "Function: {} took {} for execution.\n".format(
                func_name, datetime.now() - start
            )
        )
        return result

    return func_wrapper

@calculate_exec_time
def call_aws_service():
	st.write("Function Called!")

@calculate_exec_time
def call_local_service():
    st.write("Function Called!")

def check_sentiment():
    pass
##################################################
### Side bar elements
if "Yes" == st.sidebar.radio("Would you like to submit a feedback?", ["Yes", "No"]):
    feedback_data = st.sidebar.text_area("Your Feeback:")
    feedback_btn = st.sidebar.button('Submit', on_click=check_sentiment)


### Core design
st.title('Streamlit based NLP Application')
st.subheader('\n')
st.subheader('\n')


st.text_area("Your Text Input:", value="", height=None, max_chars=50, key=None, help="Please enter a intresing text data for classification. \nIt can be of the type Sports, Politics, business, tech, entertainment", placeholder="Please enter text to classify")


btn1, _, _, _, _, _, btn2 = st.columns([1]*6+[1.18])
# clicked = col.button('Button', on_click=call_aws_service)
button1 = btn1.button('Call AWS', on_click=call_aws_service)
button2 = btn2.button('Call Local service', on_click=call_local_service)

### Closing
st.text("Powered using AWS")

