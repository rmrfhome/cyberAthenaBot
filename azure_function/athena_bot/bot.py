from telegram import Update
from telegram.ext import Dispatcher, Updater, CallbackContext, CommandHandler
import random
import athena_bot.const as const


def advice(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(const.delhpic_maxims))

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Χαῖρε!")


handlers = {
    'start': start,
    'advice': advice,
}

def register_command_handlers(dispatcher : Dispatcher):
    for key, value in handlers.items():
        dispatcher.add_handler(CommandHandler(key, value))