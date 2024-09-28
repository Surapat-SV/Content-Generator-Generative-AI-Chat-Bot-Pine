import streamlit as st
import google.generativeai as genai

# Set up the app title and subtitle
st.title("📚 Content Generator 📚")
st.subheader("Generate a content using the AIDA framework")

# Capture Gemini API Key
gemini_api_key = st.text_input("Gemini API Key:", placeholder="Type your API Key here...", type="password")

# Initialize session state for chat history, configuration status, model instance, and introduction message status
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "gemini_configured" not in st.session_state:
    st.session_state.gemini_configured = False
if "introduction_sent" not in st.session_state:
    st.session_state.introduction_sent = False
if "model" not in st.session_state:
    st.session_state.model = None

# Configure Gemini Model if API key is provided and not configured yet
if gemini_api_key and not st.session_state.gemini_configured:
    try:
        genai.configure(api_key=gemini_api_key)
        st.session_state.model = genai.GenerativeModel("gemini-pro")
        st.success("Gemini API Key successfully configured.")
        st.session_state.gemini_configured = True

        # Send introduction message if not already sent
        if not st.session_state.introduction_sent:
            introduction_message = (
                "Hello! My name is N'Assist, your Content Creator Intern. "
                "I’m here to help you generate content using the AIDA framework. "
                "Tell me more about your product below 😊"
            )
            st.session_state.chat_history.append(("assistant", introduction_message))
            st.session_state.introduction_sent = True

    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")

# Display previous chat history
for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)

# User input for content context
st.write("### Content Customization")
product_or_service = st.text_input("Enter the product, service, or topic for content generation:")

# Chat input box is always visible for interaction
user_input = st.chat_input("Type your message or instructions here, e.g., 'Write a Facebook post promoting our new eco-friendly water bottle.'")

# Process the input and generate content if both fields are filled
if product_or_service and user_input:
    # Store and display user message
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("user").markdown(user_input)

    # Use the configured model to generate content using AIDA
    if st.session_state.model:
        try:
            # Generate AIDA content
            prompt = (
                f"Generate a persuasive content piece using the AIDA framework for the following context: {product_or_service}. "
                "Structure the content with four sections: Attention, Interest, Desire, and Action. "
                f"Here are the instructions provided by the user: {user_input}. "
                "Make each section engaging and tailored to capture the audience's attention, spark interest, create desire, and prompt action."
            )
            response = st.session_state.model.generate_content(prompt)
            bot_response = response.text  # Assuming response.text contains the generated content

            # Display generated content as AIDA sections
            st.write("### Generated Content (AIDA Framework)")
            sections = ["Attention", "Interest", "Desire", "Action"]
            for i, section in enumerate(bot_response.split('\n\n'), 1):
                if i <= len(sections):
                    st.write(f"**{sections[i-1]}**")
                    st.write(section)
                else:
                    st.write(section)

            # Store and display the response in chat history
            st.session_state.chat_history.append(("assistant", bot_response))
            st.chat_message("assistant").markdown(bot_response)

        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")
