import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as pt 
import numpy as np 
import seaborn as sns
import plotly as px

#read a csv file
#import csv file
#convert file to dataframe


df = pd.read_csv("diabetes.csv")
st.markdown("# First Five Items")
st.write(df.head())

st.markdown('# Last Ten Items')
st.write(df.tail(10))

st.title("General Information About Diabetes Analysis")
st.markdown('# Overview')
hall = df.describe
st.write(hall)

st.markdown("### OVERVIEW")
summary = df.shape
st.write(summary)

#Univariate Analysis
st.markdown("## Univariate Analysis")
st.markdown("### Blood Pressure")
df = pd.read_csv("diabetes.csv")
BloodPressure = df["BloodPressure"].describe()
st.write(BloodPressure)

st.markdown("## Chart Representation")
BP = px.bar(df["BloodPressure"], y = "BloodPressure", title = "index")
st.plotly_chart(BP, use_container_width = True)



st.title('Blood Pressure Chart')
counted = df["BloodPressure"].value_counts().reset_index()
counted.columns = ["BloodPressure", "count"] 
BloodPressure = px.pie(counted, names = "BloodPressure", values = "count", title = "Cleansheets")
st.plotly_chart(BloodPressure, use_container_width = True)




#import -m pip install scikit-learn
#import -m pip install matlib
#download seaborn- python -m pip install seaborn 