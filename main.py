import streamlit as st
import os

file = "D:\\$FILES\\SCHOOL_FILES\\#Fourth_Year\\First_Semester\\CSIT342_Industry_Elective_3\\MidtermProject\\MidtermProjectIE3\\main.py"
thisfile = os.path.abspath(file)
if ('/' in thisfile): os.chdir(os.path.dirname(thisfile))

# -- PAGE SETUP --

profile_1_page= st.Page(
    
    page="MProject/views/mainpage.py",
    title="Introduction",
    icon=":material/home:",
    default=True,
)

profile_2_page= st.Page(
    
    page="MProject/views/dataPage.py",
    title="Existing Dataset Dashboard",
    icon=":material/analytics:",
)

profile_3_page= st.Page(
    
    page="MProject/views/rawDataPage.py",
    title="Insert Raw Data",
    icon=":material/note_add:",
)

profile_4_page= st.Page(
    
    page="MProject/views/membersPage.py",
    title="Members",
    icon=":material/group:",
)


# NAVIGATION SETUP

pg = st.navigation(
    {
        "Home": [profile_1_page],
        "Data Visualization": [profile_2_page, profile_3_page],
        "BaoBao": [profile_4_page],
    }    
)

# SHARED ON ALL PAGES
st.sidebar.text("For CSIT342 - Industry Elective 3")


# RUN NAVIGATION
pg.run()