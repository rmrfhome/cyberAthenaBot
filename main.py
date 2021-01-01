from dotenv import load_dotenv
import os
import sys
import settings
from telegram.ext import Updater

sys.path.insert(0, "azure_function")
import athena_bot.bot as athena_bot

load_dotenv(verbose=True)
TOKEN = os.getenv("TELEGRAM_TOKEN")

def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)
    athena_bot.register_command_handlers(updater.dispatcher)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()