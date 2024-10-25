📚 Content Generator 📚

Welcome to the Content Generator app! 

This project allows you to generate content using the AIDA (Attention, Interest, Desire, Action) framework or engage in friendly chit-chat using a generative AI model from Gemini.

🚀 Features
AIDA Framework Content Generation: Generate persuasive content pieces tailored to your product or service using the AIDA structure. Perfect for marketing copy, product descriptions, and more.

Interactive Chatting: Enjoy friendly and engaging conversations with N'Assist, the Content Creator Intern, when not providing specific content generation tasks.
User-Friendly Interface: Simple input fields for API keys and content instructions, making the tool easy to use for anyone.

🛠️ Technologies
Streamlit: Provides the user interface for interacting with the generative AI and displaying results.
Gemini Generative AI: Powers the content generation and conversational abilities.
Python: The main programming language used for the backend logic and interaction with Gemini's API.

📋 Prerequisites
Python 3.7+: Make sure Python is installed on your system.
Streamlit: Install Streamlit using pip:
```
pip install streamlit
```
Gemini API Key: You will need a valid Gemini API key to interact with the generative AI model. Obtain this from the Gemini developer console.

💻 Installation
Clone the Repository:
```
git clone https://github.com/your-username/content-generator.git
cd content-generator
```
Install Dependencies:
```
pip install -r requirements.txt
```
Run the App:
```
streamlit run app.py
```
Open the provided URL in your browser to access the app.

🔑 Configuration
Enter the Gemini API Key: After launching the app, enter your Gemini API key in the input field to configure the generative AI model.
Start Generating: Provide a product, service, or topic, and interact with N'Assist through the chat interface to generate tailored content or just chat for fun.

🧠 How It Works
Session Management: Keeps track of chat history, configuration status, and user inputs using Streamlit's session_state.
Content Generation: When a product or service is provided, the app uses the AIDA framework to generate content through a call to the Gemini generative AI model.
Chit-Chat Mode: If no product is specified, the app switches to a casual conversation mode, offering an engaging chat experience until content generation is requested.

🤖 Example Prompts
AIDA Content: "Write a Facebook post promoting our new eco-friendly water bottle."
Chit-Chat: "Tell me a fun fact!"

🐛 Troubleshooting
Model Configuration Error: If an error occurs while configuring the Gemini model, check if the API key is correct and has the necessary permissions.
Streamlit Issues: Ensure that all required libraries are installed and that you are running the app in the correct Python environment.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing
Contributions are welcome! Please open an issue to discuss what you would like to change or add.
