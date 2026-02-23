import streamlit as st

st.title("User Registration Form")

import streamlit as st

st.markdown("""
    <style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        height: 40px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Smart Registration Form")

with st.form("registration_form"):
    name = st.text_input("Full Name")
    password = st.text_input("Password", type="password")
    gender = st.radio("Gender", ["Male", "Female", "Other"])
    agree = st.checkbox("I agree to terms and conditions")

    submit = st.form_submit_button("Register")

if submit:
    if agree:
        st.success(f"Welcome {name}! 🎉")
    else:
        st.error("You must agree to the terms.")
with st.form("user_form"):

    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=1, max_value=100)
    city = st.selectbox("Select your city", ["New York", "London", "Paris"])
    email = st.text_input("Enter your email")
   
    submitted = st.form_submit_button("Submit")


if submitted:
    st.success("Form Submitted Successfully ✅")
    st.write("### Submitted Details:")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("City:", city)
    st.write("Email:", email)