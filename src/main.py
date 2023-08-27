
import re
import telegram

from telegram import Update
from bot import *
from telegram.ext import (
    Application,
    CommandHandler,
   # ContextTypes,
   # ConversationHandler,
    MessageHandler,
   # filters,
)


#
# Constants
#
BOT_TOKEN = "6210165185:AAFr9ATj95TXkbDC7pjrEklfDouTuIMw2NY"
REVIEW, INFO = range(2)

def main() -> None:

  # Initialize the telegram bot with our bot token
  application = Application.builder().token(BOT_TOKEN).build()
  
  #yes_no_regex = re.compile(r'^(да|нет|ja|nein)$', re.IGNORECASE)

  # Create our ConversationHandler, with only one state
  handler = telegram.ext.ConversationHandler(
    entry_points = [CommandHandler('start', start),CommandHandler('faq', faq), CommandHandler('exit', exit)],

    states = {
      REVIEW: [MessageHandler('review', review)],
      INFO: [MessageHandler('info', info)],
    },
    
    fallbacks = [CommandHandler('exit', exit)],

  )
  
  application.add_handler(handler)

  # Start the bot until the user presses Ctrl-C
  application.run_polling(allowed_updates = Update.ALL_TYPES)

if __name__ == '__main__':
  main()