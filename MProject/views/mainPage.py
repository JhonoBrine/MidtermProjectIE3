import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff

st.title('BaoBao')
st.write("For Midterm Presentation")

# Load the dataset
df_sample = pd.read_csv("MProject/assets/csv/Student_Grades.csv")

# Display raw data
st.write("Raw Data:")
st.write(df_sample)

