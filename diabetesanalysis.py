import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as pt 
import numpy as np 
import seaborn as sns
import plotly.express as px

#read a csv file
#import csv file
#convert file to dataframe


df = pd.read_csv("diabetes.csv")
st.markdown("# First Five Items")
st.write(df.head())

st.markdown('# Last Five Items')
st.write(df.tail(5))

st.title("General Information About Diabetes Analysis")
st.markdown('# Overview')
Preview = df.describe
st.write(Preview)

st.markdown("### OVERVIEW")
summary = df.shape
st.write(summary)

#Univariate Analysis
st.markdown("## Univariate Analysis")
st.markdown("### Blood Pressure")
df = pd.read_csv("diabetes.csv")
BloodPressure = df["BloodPressure"].describe()
st.table(BloodPressure)


st.markdown("### Body Mass Index")
df = pd.read_csv("diabetes.csv")
Body Mass Index = df["BMI"].describe()
st.write(df["BMI"].describe())

BP = px.bar(df["BloodPressure"], y = "BloodPressure", title = "Distribution of Blood Pressure")
st.plotly_chart(BP, use_container_width = True)
pandas.DF
pd.df([BloodPressure], df[Pregnancies])


st.markdown("## Chart Representation")
BP = px.bar(df["BloodPressure"], y = "BloodPressure", title = "index")
st.plotly_chart(BP, use_container_width = True)



st.title('Blood Pressure Chart')
counted = df["BloodPressure"].value_counts().reset_index()
counted.columns = ["BloodPressure", "count"] 
BloodPressure = px.pie(counted, names = "BloodPressure", values = "count", title = "Pregnancies")
st.plotly_chart(BloodPressure, use_container_width = True)




#import -m pip install scikit-learn
#import -m pip install matlib
#download seaborn- python -m pip install seaborn 