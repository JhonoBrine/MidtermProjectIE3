import streamlit as st

st.title("📊 Conclusion Page")

st.header("General Insights")
st.write("A summary of key performance indicators based on the data gathered:")

col1, col2 = st.columns(2)

st.text("")

with col1:   

    st.text("")

    st.subheader("1. Hours Spent Studying")
    st.write("""
    - **Average:** 5 hours
    - **Range:** 1.1 to 9.2 hours
    - **Standard Deviation:** 2.52 hours
    """)
    st.write("This suggests students have varied study hours, with some dedicating significantly more time than others.")
        
    st.text("")

    st.subheader("2. Practice Sessions")
    st.write("""
    - **Average:** 2.76 sessions
    - **Range:** 0.2 to 6.2 sessions
    - **Observation:** Some students are not engaging enough in practice, while others are more consistent.
    """)
st.text("")

with col2:

    st.text("")

    st.subheader("3. Teamwork Participation")
    st.write("""
    - **Average:** 1.81 participation points
    - **Range:** 0 to 6 points
    - **Standard Deviation:** 1.7 points
    """)
    st.write("There's a significant variation in teamwork participation, suggesting some students engage more than others.")

    st.text("")

    st.subheader("4. Exam Scores")
    st.write("""
    - **Midterm Average:** 4.92 (Range: 2 to 9)
    - **Final Exam Average:** 5.35 (Range: 1.9 to 9.7)
    """)
    st.write("Final exam scores show a slight improvement compared to midterm results.")


# Overall Scores
st.subheader("5. Overall Scores")
st.write("""
- **Range:** 17 to 95
- **Mean Score:** 51.48
- **Standard Deviation:** 25.29
""")
st.write("The data reveals a bimodal distribution with a significant number of students scoring below the mean, while others excel.")

# Key Takeaways Section

st.text("")
st.text("")

st.header("Key Takeaways")
st.write("""
- **Performance Variability:** There's a wide spread in performance across study time, practice, and exam scores. Different approaches to studying are likely influencing the outcomes.
- **Study Time Correlation:** Students who spend more time studying tend to perform better across exams and overall scores.
- **Challenges for Low-Scoring Students:** A considerable number of students are struggling, suggesting a need for targeted support and interventions.
""")

st.write("This analysis can guide improvements in teaching methods, focusing on collaborative learning and supporting lower-performing students.")


# import streamlit as st
# import pandas as pd

# st.title("Conclusion Page")

# # df_sample = pd.read_csv("MProject/assets/csv/Student_Grades.csv")

# st.write("### General Insights:")
# # st.dataframe(df_sample)


# st.write(
#     """
#     ##### 1. Hours Spent Studying: 

#     - The average number of hours spent studying is approximately 5 hours. 
#     - The range spans from as low as 1.1 hours to a maximum of 9.2 hours.The standard deviation of 2.52 indicates that students have varied study hours, with some dedicating more time than others.

#     ##### 2. Practice Sessions:

#     - On average, students engage in around 2.76 practice sessions with a minimum of 0.2 sessions and a maximum of 6.2
#     - This Suggests some students are not engaging much in practice, while others are more consistent.

#     ##### 3. Teamwork Participation:

#     - The teamwork involvement is relatively low on average at 1.81. There are students with no involvement(minimum of 0) while some of students have high teamwork engagement, reaching up to 6.
#     - The data shows a significant spread, with a standard deviation of 1.7, indicating that not all students participate equally in teamwork.

#     ##### 4. Midterm and Final Exam Scores:

#     - The midterm exam scores range from 2 to 9, with an average of 4.92, while the final exam scores range from 1.9to 9.7, with an average of 5.35.
#     - These scores suggest that students' performance is fairly consistent between the two exams, with a slight increase in the final exam scores.
    
#     ##### 5. Overall Scores:

#     - The overall scores range from 17 to 95, with a mean score of 51.48. The standard deviation of 25.29 suggests a wide spread in the students'performance, with a significant number of students scoring below the mean.
#     - A bimodal pattern in the overall scores can be expected, with some students excelling and others struggling.

#     """
# )
# st.write(
#     """
#     ##### Key Takeaways:
    
#     - **Performance Variability**: There's a considerable spread in student performance across different metrics such as hours spent studying, practice sessions, and exam scores. This suggests that students follow different approaches to studying, which impacts their final outcomes.      
#     - **Correlation Between Study Time and Scores**: Higher overall scores are likely associated with more hours spent studying, as students who dedicate more time to their studies tend to perform better in exams and overall.
#     - **Low-Scoring Students**: A notable portion of students seems to struggle, as indicated by the minimum and 25th percentile values, which are quite far from the maximum, pointing towards potential gaps in understanding or engagement in the course.

#     This analysis could guide improvements in teaching methods, encouraging more collaborative learning through increased teamwork and offering additional support to lower-performing students.
#     """
# )
