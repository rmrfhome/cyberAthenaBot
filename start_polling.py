import sys
sys.path.insert(0, "azure_function")
from dotenv import load_dotenv
import os
from telegram.ext import Updater
import bot.command_handlers as handlers

load_dotenv(verbose=True)
TOKEN = os.getenv("TELEGRAM_TOKEN")


def main():
    updater = Updater(TOKEN, use_context=True)
    handlers.register(updater.dispatcher)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()