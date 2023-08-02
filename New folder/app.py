from flask import Flask, request
from ultrabot import ultraChatBot
app = Flask(__name__)


# Load environment variables from .env file
# os.getenv('OPENAI_API_KEY')


@app.route('/')
def home():
    if request.method == 'POST':
        bot = ultraChatBot(request.json)
        return bot.Processingـincomingـmessages()


if __name__ == "__main__":
    app.run(debug=True)