import streamlit as st

st.title("BaoBao")

members = [
    {"name": "Gil Joshua Yabao", "image": "assets/joshua.jpg", "role": "Leader"},
    {"name": "Jhon Lorenz Pabroa", "image": "assets/pabs.jpg", "role": "Member"},
    {"name": "Rey Dante Garcia", "image": "assets/rey.jpg", "role": "Member"},
    {"name": "Trisha Mae Rivera", "image": "assets/trisha.jpg", "role": "Member"},
    {"name": "Mark Edwin Huyo-a", "image": "assets/mark.jpg", "role": "Member"},
]

leader = next(member for member in members if member["role"] == "Leader")

st.markdown("<h2 style=' color: #0073e6;'>Team Leader</h2>", unsafe_allow_html=True)
leader_col = st.container()
with leader_col:
    st.image(leader["image"], width=200, caption=f"{leader['name']}")

st.write("")
st.markdown("<h2 style='color: #0073e6;'>Members</h2>", unsafe_allow_html=True)
columns = st.columns(2)

for i, member in enumerate(members):
    if member["role"] == "Member":
        with columns[i % 2]:
            st.image(member["image"], width=200, caption=f"{member['name']}")
