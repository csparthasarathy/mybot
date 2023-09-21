import streamlit as st
import nltk
import numpy as np
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
import pickle
import random
import json

# Download NLTK data
nltk.download('popular')

# Load the pre-trained model and data
model = load_model('model.h5')
words = pickle.load(open('texts.pkl', 'rb'))
classes = pickle.load(open('labels.pkl', 'rb'))
intents = json.loads(open('intents.json').read())
lemmatizer = WordNetLemmatizer()

# Functions for text processing and chatbot response
# ...

# Streamlit app
st.title("Chatbot")

# CSS for styling the chat interface
css = """
    .chat-container {
        display: flex;
        flex-direction: column;
        padding: 20px;
        max-width: 500px;
        margin: auto;
        border: 2px solid #f63366;
        border-radius: 10px;
        background-color: #f9f9f9;
    }
    .user-message {
        background-color: #f63366;
        color: white;
        border-radius: 10px;
        padding: 10px;
        max-width: 70%;
        margin-bottom: 10px;
    }
    .bot-message {
        background-color: #44b3b5;
        color: white;
        border-radius: 10px;
        padding: 10px;
        max-width: 70%;
        margin-bottom: 10px;
        align-self: flex-end;
    }
    .input-box {
        width: 70%;
        padding: 10px;
        border-radius: 5px;
        border: 2px solid #f63366;
        margin: 10px 0;
        resize: none;
        font-size: 16px;
    }
"""

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Function to display chat interface
def chat_interface():
    st.markdown('<div class="chat-container" id="chat-container"></div>', unsafe_allow_html=True)

# Display the chat interface
chat_interface()

# User input for chat
user_input = st.text_input("You", key="user_input", max_chars=200)
if user_input:
    st.markdown('<div class="user-message">{}</div>'.format(user_input), unsafe_allow_html=True)

# Button to send message
if st.button("Send"):
    if user_input:
        bot_response = chatbot_response(user_input)
        st.markdown('<div class="bot-message">{}</div>'.format(bot_response), unsafe_allow_html=True)
