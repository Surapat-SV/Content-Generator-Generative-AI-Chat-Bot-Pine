import streamlit as st

st.title("🐱 My chatbot app")
st.subheader("Conversation")

# Initialize session state for storing chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Initialize with an empty list

# Display all chat messages
for message in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(message)

# Capture user input and append to chat history
if prompt := st.chat_input("Type your message here ..."):
    st.session_state.chat_history.append(prompt)
    st.chat_message("user").markdown(prompt)
