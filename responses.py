
import re
import bs4
import requests

# pip3 install 

def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","sup"):
        return "Hey! How's it going?"

    return "I no understand you"

def start_text():
    start_text = """
alas, young padawan!
you have finally arrived ~

this dice roll is the last part of the (6 part survey)
congrats for hanging in there :)

ARE YOU FEELING LUCKY?
click /rules_of_the_game next
"""
    return start_text

def rules_text():
    rules_text="""
THE RULES OF THE GAME 
(as in the google form):

the bot counter will keep track of your score :) 
no need mental sums
since the params as mentioned earlier
means you can score a max of 30 (6x5)

-you only get 1 round/ try/ attempt :3 (submit the 1st score)
-you are to report the score in the google survey once you're done 
-can add your tele handle in the google form (if you wanna be part of the draw*)
-click /help if you need help 

*T&Cs
the top 10 scores will be part of the pool 
for a randomised draw of 5 winners for a ($10 GrabFood voucher each)
(you will be contacted from 25 Nov 2021 onwards)

may the odds be ever in ur favour~
click /roll_dice to start game LEGGO :)
"""
    return rules_text

# a=rules_text()
# print(a)

def help_text():
    help_text="""
-please be kind to me! only use /roll_dice 1x 
and report your score right after to complete your survey
(no spams pls :)
-use the telebot menu for list of instructions
-or pm @prispearls to ask for helps

    """
    return help_text

    