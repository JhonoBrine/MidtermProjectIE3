import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff

# Title and subtitle
st.title('BaoBao - Midterm Presentation')
st.subheader("Exploring Factors Influencing Student Performance")

# Concise Introduction
st.markdown("""
### Introduction

This project explores a dataset from **Kaggle** that focuses on student performance. Kaggle is a platform known for providing datasets and hosting data science competitions. The dataset includes:

- Hours of study
- Practice hours
- Teamwork involvement
- Midterm and final exam scores
- Overall scores and grades

The goal is to analyze how these factors relate to academic performance and identify patterns that may help improve educational outcomes.

### Dataset Overview

The dataset contains several columns that represent key academic and behavioral attributes. The raw data shows individual students' study habits, exam scores, and final grades, providing insight into their overall academic performance.
""")

# Load the dataset
df_sample = pd.read_csv("MProject/assets/csv/Student_Grades.csv")

# Adding column names to your dataset
df_sample.columns = ['Study Hours', 'Practice Hours', 'Teamwork Involvement', 'Midterm Score', 
                     'Final Score', 'Overall Score', 'Grade']

# Display raw data
st.write("### Raw Data:")
st.dataframe(df_sample)

# Displaying summary statistics with explanation
st.write("""
### Summary Statistics

The summary statistics provide a quick overview of the key attributes in the dataset. For each numeric column, you can see:

- **Count**: Number of entries in the dataset.
- **Mean**: The average value.
- **Standard deviation (std)**: The spread or variability of the data.
- **Minimum (min)**: The smallest value in the dataset.
- **25th, 50th, 75th percentiles**: These represent the data distribution, giving an idea of where most values lie.
- **Maximum (max)**: The largest value in the dataset.

Below is the summary of these statistics for the student performance dataset:
""")
st.write(df_sample.describe())
