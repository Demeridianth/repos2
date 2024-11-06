import os
import telebot
import time
from threading import Thread
import schedule

BOT_TOKEN = '...my_bot_token...'

bot = telebot.TeleBot(BOT_TOKEN)
bot_test_group_id = '-1001974322497'


# answers to these commands
def command_intake():
    @bot.message_handler(commands = ['start', 'hello'])
    def send_welcome(message):
        bot.reply_to(message, "Hello there")

    @bot.message_handler(commands = ['about'])
    def send_welcome(message):
        bot.reply_to(message, "i'm a bot in the works...")


# answers to everything
# @bot.message_handler(func = lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


# time schedule for when to run this
def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)

def timed_message():
    bot.send_message(chat_id = bot_test_group_id, text = 'your code works')

def schedule_execution():
    schedule.every().day.at("18:34").do(timed_message)
    Thread(target=schedule_checker).start()


if __name__ == '__main__':
    print('starting up the bot...')

    schedule_execution()

    command_intake()
    
    print('polling...')
    bot.infinity_polling()

