import logging
import os
import azure.functions as func
from telegram import Bot, Update
from telegram.ext import Dispatcher, Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import athena_bot.bot as athena_bot


TOKEN = os.environ["TELEGRAM_TOKEN"]
bot = Bot(TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)
athena_bot.register_command_handlers(dispatcher)


def main(req: func.HttpRequest) -> func.HttpResponse:
    request_body_dict = req.get_json() 
    update = Update.de_json(request_body_dict, bot) 
    dispatcher.process_update(update)
    logging.info(req.get_json())
    return func.HttpResponse(body='', status_code=200)
