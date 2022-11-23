import streamlit as st
import pandas as pd
import pickle

st.title("--Insert title here--")

# import model
model = pickle.load(open("milk_pred.pkl", "rb"))

st.write('Insert feature to predict')

# user input
ph = st.slider(label='pH', min_value=3.0, max_value=9.5, value=6.5, step=0.1)
temp = st.slider(label='Temprature', min_value=34, max_value=90, value=40, step=1)
taste = st.selectbox(label='Taste', options=['Good', 'Bad'], key=0)
odor = st.selectbox(label='Odor', options=['Good', 'Bad'], key=0)
fat = st.selectbox(label='Fat', options=['High', 'Low'], key=1)
turb = st.selectbox(label='Turbidity', options=['High', 'Low'], key=1)
color = st.number_input(label='Colour', min_value=240, max_value=255, value=245, step=1)

# convert into dataframe
data = pd.DataFrame({'pH': [ph],
                'Temprature': [temp],
                'Taste': [taste],
                'Odor':[odor],
                'Fat': [fat],
                'Turbidity': [turb],
                'Colour': [color]})

# model predict
clas = model.predict(data).tolist()[0]

# interpretation
st.write('Classification Result: ')
if clas == 0:
    st.text('Low')
elif clas == 1:
    st.text('Medium')
else:
    st.text('High')


