import streamlit as st
import pandas as pd
import numpy as np
import math 


primaryColor="#1e8449"
backgroundColor="#f7f9f9"
secondaryBackgroundColor="#F0F2F6"
textColor="#31333F"
font="sans serif"


st.title('Jermit Gunning: Designing the perfect car Python App')
st.header("Fill in the attributes to make your perfect car")
x = st.text_input('First hoose your Car name')
#df = pd.read_csv("Streamlit sa.csv")
st.header(f"{x}: Now that you have a name lets choose a powertrain")
col1,col2,col3 = st.columns(3)
button = col1.checkbox('Naturally Aspirated V12')
button1 = col2.checkbox('Hybrid Turbo V6')
button2 = col3.checkbox('Triple Electric Motors')
y = button
st.header("Okay now lets pic some attributes for your car")
###Columns
col1, col2 = st.columns(2)
Top_speed= col1.number_input("Power (0-100)", min_value=0, max_value = 100)
Acceleration = col1.number_input("Acceleration (0-100) " , min_value=0, max_value = 100)
Handling = col2.number_input("Handling (0-100) ", min_value=0, max_value = 100)
Weight =  col2.number_input("Weight", min_value=1000, value=1500, max_value=5000)
#st.slider("How", min_value=1, value=1, max_value=10)
Car_score = Top_speed + Acceleration + Handling
avg_car_score = Car_score/3
reliability = range(10)
#Quarter_Mile = (((Weight /10) - 50)/ 2) + (avg_car_score -50)
Quarter_mile = Weight/50 + (Top_speed)
zerotosixty =  ((((Acceleration * 100) + Weight) /1000) * .75) / 4


#st.header('Car scoring')
#col1 = st.columns(1)
#Avg_score = col1.car_score
#st.write(avg_car_score)
#st.write(reliability)

col1, col2,col3 = st.columns(3)
col1.metric(label="Overall Rating", value=f"{avg_car_score:,.2F}")
#col2.metric(label="Average Annual repair cost", value=f"${1000:,.0f}")
col2.metric(label="0-60 Time", value=f"{zerotosixty:,.2F}")
col3.metric(label="Top Speed MPH",  value=f"{Quarter_mile:,.2F}")



sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")

#st.checkbox("label")

#data = pd.read_csv("Streamlit sa.csv")
#st.write(data)
