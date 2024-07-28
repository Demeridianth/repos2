import os
import telebot
import time
from threading import Thread
import schedule

BOT_TOKEN = '6665008311:AAGlv-rXB2b6jWEopn7mTiIegGFP4ERqRsM'

bot = telebot.TeleBot(BOT_TOKEN)
bot_test_group_id = '-1001974322497'


def command_intake():
    """ отвечает на команды """
    @bot.message_handler(commands = ['start', 'hello'])
    def send_welcome(message):
        bot.reply_to(message, "Hello there")

    @bot.message_handler(commands = ['about'])
    def send_welcome(message):
        bot.reply_to(message, "i'm a bot in the works...")


"""" (ECHO) отвечает на всё подряд """
# @bot.message_handler(func = lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


""" График выполнения функции """
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

