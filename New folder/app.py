from flask import Flask, request
from ultrabot import ultraChatBot
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        bot = ultraChatBot(request.json)
        return bot.Processingـincomingـmessages()


if __name__ == "__main__":
    app.run(debug=True)