import streamlit as st
import pandas as pd
import numpy as np
import math 


primaryColor="#1e8449"
backgroundColor="#f7f9f9"
secondaryBackgroundColor="#F0F2F6"
textColor="#31333F"
font="sans serif"

tab1,tab2 = st.tabs(["Car Customizer", "Word Finder"])

with tab1:
    st.title('Jermit Gunning: Car Attributes Python App')
    st.sidebar.header("Welcome to my App")
    st.header("First you can reach me here:")
    col1, col2, col3 = st.columns(3)


    link = col1.link_button("LinkedIn", "https://www.linkedin.com/in/jermit-gunning-779a81172/")
    link1 = col2.link_button("Portfolio", "https://sites.google.com/view/jermitgunning/home")
    link3 = col3.link_button("Other Apps", "https://share.streamlit.io/user/spt-bmi")
    st.header("Instructions")
    st.write("Fill out the attributes below to build your car and get an IRL comparison")
    x = st.text_input('First choose your Car name')
#df = pd.read_csv("Streamlit sa.csv")
    st.header(f"{x} Now that you have a name let's choose a powertrain")
    col1,col2,col3 = st.columns(3)
    button = col1.checkbox('Naturally Aspirated V12')
    button1 = col2.checkbox('Hybrid Turbo V6')
    button2 = col3.checkbox('Triple Electric Motors')
    y = button
    st.header("Okay now let's pic some attributes for your car")
###Columns
    col1, col2 = st.columns(2)
    Top_speed= col1.number_input("Power (0-100)", min_value=0, max_value = 100)
    Acceleration = col1.number_input("Acceleration (0-100) " , min_value=0, max_value = 100)
    Handling = col2.number_input("Handling (0-100) ", min_value=0, max_value = 100)
    Weight =  col2.number_input("Weight", min_value=2000, value=2000, max_value=5000)
#st.slider("How", min_value=1, value=1, max_value=10)
    Car_score = Top_speed + Acceleration + Handling
    avg_car_score = Car_score/3
    reliability = range(10)
#Quarter_Mile = (((Weight /10) - 50)/ 2) + (avg_car_score -50)
    Quarter_mile = Weight/50 + (Top_speed)
    zerotosixty =  ((((Weight) /1000) * 2)) - (Acceleration/55)

#st.header('Car scoring')
#col1 = st.columns(1)
#Avg_score = col1.car_score
#st.write(avg_car_score)
#st.write(reliability)


#x = st.text_input('First choose your Car name')

#speed = st.text_input("Okay now let's pic some attributes for your car")


#st.bar_chart(speed)

    col1, col2,col3 = st.columns(3)
    col1.metric(label="Overall Rating", value=f"{avg_car_score:,.2F}")
#col2.metric(label="Average Annual repair cost", value=f"${1000:,.0f}")
    col2.metric(label="0-60 Time", value=f"{zerotosixty:,.2F}")
    col3.metric(label="Top Speed MPH",  value=f"{Quarter_mile:,.2F}")



    sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
    selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")

#st.image("DSC00008.JPG")
#st.checkbox("label")

#data = pd.read_csv("Streamlit sa.csv")
#st.write(data)
with tab1:
    st.header("Your Car Comparsion")
    y = zerotosixty
if y <2.5:
    st.write("Ferrari - You have a thing for speed huh?")
else:
    st.write("PT Cruiser - Well maybe you won't get there soon but you'll get there")

with tab2:
    st.header('In this tab we are you can input a word and see how many characters it has')


       xx = st.text_input('Put in word here')
    
with tab2: 
    def badmon_function(xx):
        st.write('This sentence has', len(xx), 'characters' )

with tab2:
    st.subheader(badmon_function(xx))

    
