import streamlit as st

# Title of the page
st.title("Members")

# List of member names and their corresponding image paths
members = [
    {"name": "Jhon Lorenz Pabroa", "image": "assets/pabs.jpg"},
    {"name": "Rey Dante Garcia", "image": "assets/rey.jpg"},
    {"name": "Gil Joshua Yabao", "image": "assets/joshua.jpg"},
    {"name": "Trisha Mae Rivera", "image": "assets/trisha.jpg"},
    {"name": "Mark Edwin Huyo-a", "image": "assets/mark.jpg"},
]

# Create a 3-column layout
columns = st.columns(3)

# Loop through members and display images in columns
for i, member in enumerate(members):
    with columns[i % 3]:  # Cycle through columns
        st.image(member["image"], width=200)
        st.markdown(f"<h3 style='font-size: 20px; font-weight: bold;'>{member['name']}</h3>", unsafe_allow_html=True)
