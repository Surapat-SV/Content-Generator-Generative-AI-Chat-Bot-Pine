import streamlit as st
import google.generativeai as genai

# Set up the app title and subtitle
st.title("📚 Content Generator 📚")
st.subheader("Generate content using the AIDA framework or just enjoy a chat!")

# Capture Gemini API Key
gemini_api_key = st.text_input("Gemini API Key:", placeholder="Type your API Key here...", type="password")

# Initialize session state for chat history, configuration status, model instance, introduction status, guidance flag, and chit-chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "gemini_configured" not in st.session_state:
    st.session_state.gemini_configured = False
if "introduction_sent" not in st.session_state:
    st.session_state.introduction_sent = False
if "model" not in st.session_state:
    st.session_state.model = None
if "guidance_given" not in st.session_state:
    st.session_state.guidance_given = False  # Tracks if the user has been reminded to provide product/service
if "chitchat_memory" not in st.session_state:
    st.session_state.chitchat_memory = []  # Stores up to 10 chit-chat messages from the user
if "chitchat_count" not in st.session_state:
    st.session_state.chitchat_count = 0  # Tracks the number of chit-chat interactions

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
                "I’m here to help you generate content using the AIDA framework or just chat joyfully. "
                "Tell me more about your product below, or just say hi! 😊"
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

# Process the input and respond accordingly
if user_input:
    # Store and display user message
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("user").markdown(user_input)

    # Check if the product or service field is empty
    if not product_or_service:
        # Agent 2: Chit-Chat Agent takes over if no product/service is provided
        if not st.session_state.guidance_given:
            # Remind the user once about providing the product/service
            guidance_response = (
                "It seems like you haven't provided a product, service, or topic yet. "
                "Feel free to tell me about it above if you'd like me to create content for you. "
                "Otherwise, let's just chat and have some fun! 😊"
            )
            st.session_state.chat_history.append(("guidance", guidance_response))
            st.chat_message("guidance").markdown(guidance_response)
            st.session_state.guidance_given = True
        else:
            # Store chit-chat interactions in memory
            st.session_state.chitchat_memory.append(user_input)
            st.session_state.chitchat_count += 1
            
            # Send the stored chit-chat memory to Gemini for context-aware response
            if st.session_state.model:
                try:
                    # Prepare the conversation context to send to Gemini
                    conversation_context = "\n".join(st.session_state.chitchat_memory[-10:])
                    prompt = (
                        f"Continue this conversation in a friendly and engaging manner. "
                        f"Here is the conversation so far:\n{conversation_context}\n"
                        f"Respond joyfully and naturally to the user's last message: '{user_input}'"
                    )
                    response = st.session_state.model.generate_content(prompt)
                    bot_response = response.text  # Assuming response.text contains the generated response

                    # Display generated response based on the scenario
                    st.session_state.chat_history.append(("chit-chat", bot_response))
                    st.chat_message("chit-chat").markdown(bot_response)

                except Exception as e:
                    st.error(f"An error occurred while generating the response: {e}")
            
            # If user reaches 10 chit-chat interactions, politely remind them about content creation
            if st.session_state.chitchat_count >= 10:
                reminder_response = (
                    "I've enjoyed our chat so much! 🎉 I do have some content tasks to get back to, though. "
                    "Do you have any content you'd like me to help with? If so, just let me know your topic! "
                    "If not, please come back soon for another nice chat. 😊"
                )
                st.session_state.chat_history.append(("chit-chat", reminder_response))
                st.chat_message("chit-chat").markdown(reminder_response)
                
                # Reset chit-chat count and prompt for content creation
                st.session_state.chitchat_count = 0
                st.session_state.chitchat_memory.clear()

    # Use Agent 1: Content Creation Agent to generate content using AIDA
    elif st.session_state.model:
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
