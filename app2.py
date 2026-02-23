import streamlit as st

st.title("welcome to basic streamlit app")

st.slider("select a age", 1, 100, 25)
st.selectbox("select a city", ["new york", "london", "paris"])

if st.button("submit"):
 st.write("Age", st.session_state["age"], "City", st.session_state["city"])