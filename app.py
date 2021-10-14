from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Candice")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
trainer.train("./movie_booking.yml")

'''
An other way to train the chatbot
data = ['hello','Greetings!',
        'book movie tickets', 'Which movie would you like to watch?',
        'Black widow', 'Please specify the theatre.',
        'INOX', 'Sorry, the bookings are not opened yet. Come back soon.',
        'who developed you', "I was built by 'Sai Teja Erukude'. Thanks to him."]

trainer1 = ListTrainer(bot)
trainer1.train(data)
'''


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def bot_response():
    user_input = request.args.get("msg").lower()
    return str(bot.get_response(user_input))


if __name__ == "__main__":
    app.run()
