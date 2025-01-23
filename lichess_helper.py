from typing import Final
from telegram import Update
import berserk
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random
from dotenv import load_dotenv
import os
load_dotenv()

tele_token=os.getenv('TELE_API')
lc_token=os.getenv('LC_API')
username='@rating_comparison_bot'

session = berserk.TokenSession(lc_token)
client = berserk.Client(session=session)

async def start_command (update, context):
    await update.message.reply_text("This bot will compare rating of two different user or display rating of a single user")

async def handle_message(update, context):
    feed=update.message.text.strip()
    chat_type=update.message.chat.type
    if chat_type=='group':
        if username in feed:
            feed=feed.replace(username,'').strip()
        else:
            return

    print('Enter your lichess username to display stats: ')
    print(f'id is {feed}')
    try:
        feed = client.users.get_public_data(feed)
    except:
        await update.message.reply_text("No such user found or account has been closed🚫!")
        
    print(f"ID: {feed['count']['all']}")
 

    s1=f'ID: {feed['id']}'
    s2=f'Bullet : {feed['perfs']['bullet']['rating']}'
    s3=f'Blitz    : {feed['perfs']['blitz']['rating']}'
    s4=f'Rapid : {feed['perfs']['rapid']['rating']}'
    s5=f'Games: {feed['count']['all']}'
    

    s5=f"""{s1}\n{s2}\n{s3}\n{s4}\n{s5}"""

    await update.message.reply_text(s5)

   

async def your_rating_command(update, command):
    await update.message.reply_text("Enter id to check rating")
    

# Error handling
async def error(update, context):
    print(f"Update {update} caused error {context.error}")

# Main bot setup
if __name__ == '__main__':
    # print("Starting the bot...")
    app = Application.builder().token(tele_token).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('check', your_rating_command))
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Polling")
    app.run_polling(poll_interval=3)