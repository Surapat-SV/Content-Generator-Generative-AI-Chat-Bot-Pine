import streamlit as st

st.title("🐱 My chatbot app")

# Display the user input
if user_input := st.text_input("What's on your mind", placeholder="Type your message here..."):
    st.write(f"User Input: {user_input}")
