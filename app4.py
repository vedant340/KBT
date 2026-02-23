import streamlit as st
st.title("Chabot App ")
user_input = st.text_input("You: ", "Hello, Who are you?")
if st.button("Send"):
    st.write("Chatbot: ", "I'm a simple chatbot.How can I assist you today?")
if st.button("Clear"):
    st.session_state["user_input"] = "my name is vedant";
    st.session_state["chat_history"] = [];
    st.write("Chat history cleared.")    
