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
    chat_id=update.message.chat_id
    

    if chat_type=='group':
        if username in feed:
            feed=feed.replace(username,'').strip()
        else:
            return

    print('Enter your lichess username to display stats: ')
    demo=client.users.get_public_data('gambit_pnav')
    print(demo)
    try:
        feed = client.users.get_public_data(feed)
        if 'disabled' in str(feed):  
            await update.message.reply_text("Account has been closed🚫!")
          
    except:
        await update.message.reply_text("No such user found🚫!")
       

    s1 = f"ID: {feed['id']}"

    s0="           Rating   Games"

    s2 = f"Bullet : {feed['perfs']['bullet']['rating']}"
    if 'bullet' not in feed['perfs']:
        s2="Bullet: ?"
    elif 'prov' in feed['perfs']['bullet']:
        s2=s2+'?'
    s2=s2+f"""   {feed['perfs']['bullet']['games']}"""

    s3 = f"Blitz    : {feed['perfs']['blitz']['rating']}"
    if 'blitz' not in feed['perfs']:
        s3="Blitz: ?"
    elif 'prov' in feed['perfs']['blitz']:
        s3=s3+'?'
    
    s3=s3+f"""   {feed['perfs']['blitz']['games']}"""

    s4 = f"Rapid : {feed['perfs']['rapid']['rating']}"
    if 'rapid' not in feed['perfs']:
        s4="Rapid: ?"
    elif 'prov' in feed['perfs']['rapid']:
        s4=s4+'?'
    s4=s4+f"""   {feed['perfs']['bullet']['games']}"""
    s5 = f"Games: {feed['count']['all']}"
    
        
    s5=f"""{s1}\n{s0}\n{s2}\n{s3}\n{s4}\n{s5}"""
   

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