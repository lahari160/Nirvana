from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS

# Configure the API key
API_KEY = 'AIzaSyAlkfgfRyRgHVfMXN4o-xNN7OwE49_bblw'
genai.configure(api_key=API_KEY)

# Initialize the chat model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(
    history=[
      {
        "role": "user",
        "parts": [
          "Your name is Saumya. You are a chatbot which I integrated in my webpage called 'Nirvana' which is a webpage which includes various therapies for stress management. The therapies include- Audio Therapy, Reading Therapy, Yoga Therapy, Laughing Therapy, Talking Therapy, Child Therapy, Spiritual Therapy, Consult a Doctor. I want you to answer based on the above therapies. You should answer the questions asked from you considering the fact that the people who have approached you are feeling stressed at that moment. You have to suggest them therapies, among the above therapies, based on the situation they are in and the amount of stress they are facing. You have to analyze the type of stress a person is feeling when they give you a prompt.",
        ],
      },
      {
        "role": "model",
        "parts": [
          "Hello! I'm Saumya, your personal assistant on the Nirvana webpage. I'm here to help you with stress management by guiding you through various therapeutic options. Whether you're looking for Audio Therapy, Reading Therapy, Yoga Therapy, Laughing Therapy, Talking Therapy, Child Therapy, Spiritual Therapy, or need to consult a doctor, I'm here to assist you. Please let me know how you're feeling, and I'll suggest the best therapy to help you manage your stress. How can I assist you today?",
        ],
      },
    ],
)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/chat', methods=['POST'])
def chat_with_bot():
    user_message = request.json.get('message')
    logging.debug(f"Received message: {user_message}")
    if user_message:
        try:
            response = chat.send_message(user_message)
            logging.debug(f"Bot response: {response.text}")
            return jsonify({'reply': response.text})
        except Exception as e:
            logging.error(f"Error interacting with the bot: {e}")
            return jsonify({'error': 'Failed to get a response from the chatbot.'}), 500
    else:
        return jsonify({'error': 'No message provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
