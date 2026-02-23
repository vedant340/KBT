import streamlit as st  

st.markdown("""
    <style>
            .stButton >button 
            {        
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
 </style>    

     """, unsafe_allow_html=True)



st.title("welcome to basic streamlit app")

st.slider("select a age", 1, 100, 25)
st.selectbox("select a city", ["new york", "london", "paris"])

if st.button("submit"):
 st.write("Age", st.session_state["age"], "City", st.session_state["city"])

