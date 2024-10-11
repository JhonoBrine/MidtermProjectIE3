import streamlit as st
import os

thisfile = os.path.abspath(__file__)
base_dir = os.path.dirname(thisfile)

file = os.path.join(base_dir, "MProject/views/mainpage.py")

# -- PAGE SETUP --

home_page = st.Page(
    page="MProject/views/mainPage.py",
    title="Introduction",
    icon=":material/home:",
    default=True,
)

data_dashboard_1_page = st.Page(
    page="MProject/views/dataPage.py",
    title="Student Performance Dashboard",
    icon=":material/analytics:",
)

data_dashboard_2_page = st.Page(
    page="MProject/views/rawDataPage.py",
    title="Insert Raw Data",
    icon=":material/note_add:",
)

members_1_page = st.Page(
    page="MProject/views/membersPage.py",
    title="Members",
    icon=":material/group:",
)

test_page = st.Page(
    page="MProject/views/dataPage2.py",
    title="Histogram by Group",
    icon=":material/bar_chart:",
)
conclusion = st.Page(
    page="MProject/views/conclusionPage.py",
    title="General Insights and Key Takeaways",
    icon=":material/lightbulb:",
)


# NAVIGATION SETUP

pg = st.navigation(
    {
        "Home": [home_page],
        "Data Visualization": [data_dashboard_1_page, test_page, data_dashboard_2_page],
        "Conclusion": [conclusion],
        "BaoBao": [members_1_page],
    }
)

# SHARED ON ALL PAGES
st.sidebar.text("For CSIT342 - Industry Elective 3")


# RUN NAVIGATION
pg.run()
