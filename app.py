from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Candice")                        # creating an instance of ChatBot
trainer = ChatterBotCorpusTrainer(bot)          # creating an instance of ChatterBotCorpusTrainer
trainer.train("chatterbot.corpus.english")      # training our bot with existing english corpus

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def bot_response():
    user_input = request.args.get("msg")
    return str(bot.get_response(user_input))
    
if __name__ == "__main__":
    app.run()                                   # start the Flask app