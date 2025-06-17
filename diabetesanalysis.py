import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as pt 
import numpy as np 
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



#pandas is used for data analysis
#scikitlearn is used for predictive analysis.
#read a csv file
#import csv file
#convert file to dataframe


df = pd.read_csv("diabetes.csv")
st.markdown("# First Five Observation")
st.write(df.head())

st.markdown('# Last Five Observation')
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
Body_Mass_Index = df["BMI"].describe()
st.write(df["BMI"].describe())

st.markdown("### Pregnancies")
df = pd.read_csv("diabetes.csv")
Pregnancies = df["Pregnancies"].describe()
st.write(df["Pregnancies"].describe())

st.markdown("### Skin Thickness")
df = pd.read_csv("diabetes.csv")
Skin = df["SkinThickness"].describe()
st.write(df["SkinThickness"].describe())

BP = px.histogram(df["BloodPressure"], y = "BloodPressure", title = "Distribution of Blood Pressure")
st.plotly_chart(BP, use_container_width = True)

BP2 = px.bar(df["BloodPressure"], y = "BloodPressure", title = "Distribution of Blood Pressure")
st.plotly_chart(BP2, use_container_width = True)

st.markdown("Bivariate Analysis")
st.markdown("## BloodPressure vs Pregnancies Description")
df2 = pd.DataFrame(df["BloodPressure"], df["Pregnancies"])
st.write(df2)

st.markdown("## BloodPressure vs BMI")
df3 = pd.DataFrame(df["BloodPressure"], df["BMI"])
st.write(df3)

st.markdown("## Pregnancies vs Age")
df4 = pd.DataFrame(df["Pregnancies"], df["Age"])
st.write(df4)


st.markdown("## Correlation")
correlation = df.corr()
st.write(correlation)

st.markdown("## Predictive Analysis")
X = df.drop("Outcome", axis=1)
Y = df["Outcome"]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)


model = LogisticRegression()
model.fit(X_train,Y_train) #training the model

st.markdown("## Outcome Prediction")
prediction = model.predict(X_test)
st.write(prediction)

st.markdown("## Model Evaluation")
accuracy = accuracy_score(prediction, Y_test)
st.write(accuracy)

#import -m pip install scikit-learn
#import -m pip install matlib
#download seaborn- python -m pip install seaborn 