# pip3 install python-telegram-bot

# python3 -m telegram
# python-telegram-bot 13.8.1
# Bot API 5.4
# certifi 2021.10.08
# Python 3.9.8 (main, Nov 10 2021, 09:21:22)  [Clang 13.0.0 (clang-1300.0.29.3)]

import constants as keys
from telegram.ext import *
import responses as R
import bot_roll_dice as roller

print("Bot started...")

def start_command(update, context):
    # update.message.reply_text("to start game type /start_game\nType sth random to get started!")
    msg = R.start_text()
    update.message.reply_text(msg)


def rules_of_the_game_command(update, context):
    msg = R.rules_text()
    update.message.reply_text(msg)

def roll_dice_command(update,  context):   
    list_of_roll, list_of_scores = roller.game()
    for i in range(0,len(list_of_scores)):
        msg = "Roll #{}\n>>> you rolled a: {} <<<\nYour total score is: {}\n".format(i+1, list_of_roll[i], list_of_scores[i])
        print(msg)
        update.message.reply_text(msg)

def help_command(update, context):
    msg = R.help_text()
    update.message.reply_text(msg)

def handle_message(update, context):
    text = str(update.message.text).lower() #user input text, in update as input
    response  = R.sample_response(text) #response helper function gives response
    update.message.reply_text(response)

def error():
    print("error {}".format(error))
    
def main():
    try:
        updater = Updater(keys.API_KEY, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start_command))
        dp.add_handler(CommandHandler("rules_of_the_game",rules_of_the_game_command))
        dp.add_handler(CommandHandler("roll_dice", roll_dice_command))
        dp.add_handler(CommandHandler("help", help_command))
        dp.add_handler(MessageHandler(Filters.text, handle_message))

        dp.add_error_handler(error)

        updater.start_polling() #can add sleep time
        updater.idle()

    except:
        print("check error script no compile?")


main()

# python3 /Users/ongeeling/Documents/GitHub/telebot_youtube/main.py
