import streamlit as st

st.title("Basic Calculator")
num1 = int(st.number_input("Enter first number", step=1,format="%d"))
num2 = int(st.number_input("Enter second number", step=1,format="%d"))   
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"]) 
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    st.write("Result:", result)
