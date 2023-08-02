from flask import Flask, render_template, request, redirect, url_for,jsonify
import requests
from dotenv import load_dotenv
import os
import urllib.parse
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

messages = []

# Load environment variables from .env file
load_dotenv()
# os.getenv('OPENAI_API_KEY')

token = "5d57z8cc50euqxph>"
api_url = "https://api.ultramsg.com/instance56352/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def handle_incoming_messages():
    data = request.get_json(force=True) # get_json method is used instead of request.json
    incoming_message = data['body']
    bot_message=""
    chat_id = data['from']

    
    if "hello" in incoming_message or "hi" in incoming_message or "hey" in incoming_message:
        bot_message = "Hello! How can I assist you today?"

    if "issue" in incoming_message or "problem" in incoming_message or "error" in incoming_message:
        bot_message = "I'm sorry to hear that you're experiencing issues. Please describe the problem in detail, and I'll do my best to help you."

    if "account" in incoming_message or "login" in incoming_message or "password" in incoming_message:
        bot_message = "If you're having trouble with your account, please ensure you're using the correct login credentials. If the issue persists, let me know, and I'll be glad to assist."

    if "order" in incoming_message or "shipment" in incoming_message or "delivery" in incoming_message:
        bot_message = "For questions about orders, shipments, or deliveries, please provide your order number, and I'll check the status for you."

    if "refund" in incoming_message or "return" in incoming_message or "exchange" in incoming_message:
        bot_message = "If you want to initiate a refund, return, or exchange, please visit our website's 'Returns and Refunds' page for more information."

    if "pricing" in incoming_message or "cost" in incoming_message or "payment" in incoming_message:
        bot_message = "You can find information about pricing and accepted payment methods on our website's 'Pricing' section. If you need specific details, feel free to ask!"

    if "features" in incoming_message or "capabilities" in incoming_message or "functions" in incoming_message:
        bot_message = "To learn about the features and capabilities of our product, you can check our website's 'Features' page or ask me specific questions!"

    if "contact" in incoming_message or "support team" in incoming_message or "help desk" in incoming_message:
        bot_message = "If you need to reach our support team directly, you can send an email to support@ourwebsite.com or call our helpline at +1-800-123-4567."

    if "thank you" in incoming_message or "thanks" in incoming_message or "appreciate" in incoming_message:
        bot_message = "You're welcome! If there's anything else you need assistance with, don't hesitate to ask."

    if "technical" in incoming_message or "software" in incoming_message or "hardware" in incoming_message:
        bot_message = "For technical issues, our support team can provide guidance on software and hardware-related problems. Please describe your concern in more detail."

    if "installation" in incoming_message or "setup" in incoming_message or "configure" in incoming_message:
        bot_message = "If you need assistance with product installation, setup, or configuration, our support team can walk you through the process step-by-step."

    if "compatibility" in incoming_message or "system requirements" in incoming_message:
        bot_message = "To check product compatibility with your system, please refer to our website's 'System Requirements' section or ask our support team for help."

    if "documentation" in incoming_message or "manual" in incoming_message or "guide" in incoming_message:
        bot_message = "For product documentation or user guides, you can access downloadable resources on our website or request them from our support team."

    if "cancel" in incoming_message or "terminate" in incoming_message or "suspend" in incoming_message:
        bot_message = "If you wish to cancel, terminate, or suspend a service or subscription, please contact our support team, and they will assist you with the process."

    if "privacy" in incoming_message or "data protection" in incoming_message or "GDPR" in incoming_message:
        bot_message = "We take your privacy seriously. To learn more about our data protection practices and GDPR compliance, please visit our website's 'Privacy Policy' page."

    if not bot_message:
        bot_message = "I'm sorry, I didn't quite catch that. Could you please provide more information or ask your question differently?"

    messages.append({'from': 'ChatBot', 'body': bot_message})
    url = "https://api.ultramsg.com/instance56352/messages/chat"
    payload = json.dumps({
    "token": "5d57z8cc50euqxph",
    "to": chat_id,
    "body": bot_message})
    headers = {
  'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return jsonify({"message": response.text}), 200

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == "__main__":
    app.run(debug=True)