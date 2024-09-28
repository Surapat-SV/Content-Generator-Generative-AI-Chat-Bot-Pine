import streamlit as st

st.title("🐱 My chatbot app")
st.subheader("Conversation")

# Initialize session state for storing chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Initialize with an empty list

# Display the user input
if user_input := st.chat_input("What's on your minds: ", placeholder="Type your message here..."):
    st.session_state.chat_history.append(user_input)
    
# Display all messages using st.write
for message in st.session_state.chat_history:
    st.chat_message(message)
