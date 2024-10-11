import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px

st.title('Histogram')
st.write('A histogram comparison between data grouped by Grades')

# Load the dataset
df = pd.read_csv("MProject/assets/csv/Student_Grades.csv")

grades = df['Grade'].unique()

column = st.selectbox(
    "Choose a column",
    ("Hours", "Practice", "TeamWork", "MidTerm", "FinalExam", "Scores"),
)
def plot_histograms(data, column):
    hist_data = []
    group_labels = grades
    
    for grade in data['Grade'].unique():
        # Filter data by grade
        grade_data = data[data['Grade'] == grade][column]
        hist_data.append(grade_data)
        
    fig = ff.create_distplot(hist_data, group_labels, bin_size=1)
    fig.update_layout(title="Histogram of " + column) 
    st.plotly_chart(fig, use_container_width=True)

# Call the plotting functions
plot_histograms(df, column)

st.write("Full data:")
df

