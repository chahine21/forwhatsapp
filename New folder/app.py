from flask import Flask, render_template, request, redirect, url_for,jsonify
import requests
import json
from flask_cors import CORS
from ultrabot import ultraChatBot
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


# Load environment variables from .env file
# os.getenv('OPENAI_API_KEY')


@app.route('/')
def home():
    if request.method == 'POST':
        bot = ultraChatBot(request.json)
        return bot.Processingـincomingـmessages()


if __name__ == "__main__":
    app.run(debug=True)