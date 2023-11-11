from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '6665008311:AAGlv-rXB2b6jWEopn7mTiIegGFP4ERqRsM'
BOT_USERNAME: Final = '@poleznij_bot'
MY_USER_ID: Final = '5194918222'
GROUP_ID: Final = '-1001974322497'


# Send Message

async def send_message(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=GROUP_ID, text='it works!')

# Commmands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Gods New Day!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type something so i can respond!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')


# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hy there!'
    
    if 'how are you' in processed:
        return  'I am good!'
    
    if 'i love python' in processed:
        return 'Yes i do!'
    
    return 'I do not understand what you wrote...'

#Responding to whatever USER is trying to contact the BOT
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'supergroup':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('send_message', send_message))

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Send Message to Group
 


    # Errors
    app.add_error_handler(error)

    # Polls the bot (checks for new msgs)
    print('Polling...')
    app.run_polling(poll_interval=3)

