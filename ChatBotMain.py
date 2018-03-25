##Bryce Lauritzen
##Chatbot
##Made in Python 3.6.3

#having issues with pip on the computers and getting the dependencies
#not sure if I have it right, but I think it should work

from chatterbot.trainers import ListTrainer #training the chatbot
from chatterbot import ChatBot #importing the actual chatbot

bot = ChatBot ('Test') #make the Chatbot

talk = open('BasicText.txt.','r').readlines() #loading in my set text response

bot.set_trainer(ListTrainer) #sets the trainer up

bot.train(talk) #trains the bot on our text list

while True:
    request = input('You: ') ## User input
    response = bot.get_response(request) ##Bot response

    print('Bot: ', response)

