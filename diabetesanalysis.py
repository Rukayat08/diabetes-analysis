import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as pt 
import numpy as np 
import seaborn as sns

#read a csv file
#import csv file
#convert file to dataframe

df = pd.read_csv("diabetes.csv")
st.markdown("# First Five Arguments")
st.write(df.head())
st.markdown('# Last five Arguments')
st.write(df.tail(10))


#import -m pip install scikit-learn
#import -m pip install matlib
#download seaborn- python -m pip install seaborn 