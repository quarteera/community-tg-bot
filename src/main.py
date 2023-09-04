
import configparser
import telegram

from telegram import Update
from bot import *
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

config = configparser.ConfigParser()
config.read('config.ini', encoding = 'utf-8-sig')

#
# Constants
#
API_ID = config.get('default','API_ID')
API_HASH = config.get('default','API_HASH')
BOT_TOKEN = config.get('default','BOT_TOKEN')
REVIEW, INFO = range(2)

def main() -> None:

  print('Starting bot...')
  # Initialize the telegram bot with our bot token
  application = Application.builder().token(BOT_TOKEN).build()
  
  #yes_no_regex = re.compile(r'^(да|нет|ja|nein)$', re.IGNORECASE)

  handler = telegram.ext.ConversationHandler(
    entry_points = [CommandHandler('start', start),CommandHandler('faq', faq), CommandHandler('exit', exit)],

    states = {
      REVIEW: [MessageHandler('review', review)],
      INFO: [MessageHandler('info', info)],
    },
    
    fallbacks = [CommandHandler('exit', exit)],

  )
  
  application.add_handler(handler)

  application.add_handler(MessageHandler(filters.TEXT, handle_message))

  application.add_error_handler(error)

  # Start the bot until the user presses Ctrl-C
  print('Polling bot...')
  application.run_polling(poll_interval = 3, allowed_updates = Update.ALL_TYPES)

if __name__ == '__main__':
  main()