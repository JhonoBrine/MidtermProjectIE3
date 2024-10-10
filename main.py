import streamlit as st
import os

# Set the directory where your main.py file is located
thisfile = os.path.abspath(__file__)
base_dir = os.path.dirname(thisfile)

# Adjust the path to your files relative to the base_dir
file = os.path.join(base_dir, "MProject/views/mainpage.py")

# -- PAGE SETUP --

profile_1_page= st.Page(
    
    page="MProject/views/mainPage.py",
    title="Introduction",
    icon=":material/home:",
    default=True,
)

profile_2_page= st.Page(
    
    page="MProject/views/dataPage.py",
    title="Student Performance Dashboard",
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