import telebot
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN = '6665008311:AAGlv-rXB2b6jWEopn7mTiIegGFP4ERqRsM'
user_id = '5194918222'


if __name__ == '__main__':
    
    bot = telebot.TeleBot(token=TOKEN)

    

    # def send_text(message):
    bot.send_message(chat_id='-1001974322497', text='text')

    bot.polling(none_stop=True)





