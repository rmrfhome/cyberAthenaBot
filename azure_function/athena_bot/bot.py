from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, Updater, CallbackContext, CommandHandler, CallbackQueryHandler
import random
import athena_bot.const as const
import athena_bot.latin as latin


def advice(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(const.delhpic_maxims))

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Χαῖρε!")

def test_latin(update: Update, context: CallbackContext) -> None:
    verbi = [
        ('puell', latin.Declinatio.Pirma),
        ('aqu', latin.Declinatio.Pirma),
        ('grati', latin.Declinatio.Pirma),
        ('caus', latin.Declinatio.Pirma),
        ('lingu', latin.Declinatio.Pirma),
        ('cur', latin.Declinatio.Pirma),
        ('fam', latin.Declinatio.Pirma),
        ('rot', latin.Declinatio.Pirma),
        ('form', latin.Declinatio.Pirma),
        ('tabul', latin.Declinatio.Pirma),
        ('fortun', latin.Declinatio.Pirma),
        ('vi', latin.Declinatio.Pirma),
        ('glori', latin.Declinatio.Pirma),
        ('vit', latin.Declinatio.Pirma),
    ]
    question = latin.prepare_guestion(random.choice(verbi))
    keyboard = [
        [
            InlineKeyboardButton(question[1][0][0], callback_data=question[1][0][1]),
            InlineKeyboardButton(question[1][1][0], callback_data=question[1][1][1]),
        ],
        [
            InlineKeyboardButton(question[1][2][0], callback_data=question[1][2][1]),
            InlineKeyboardButton(question[1][3][0], callback_data=question[1][3][1]),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(question[0], reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer(text=query.data)

handlers = {
    'start': start,
    'advice': advice,
    'latin': test_latin,
}

def register_command_handlers(dispatcher : Dispatcher):
    for key, value in handlers.items():
        dispatcher.add_handler(CommandHandler(key, value))
    dispatcher.add_handler(CallbackQueryHandler(button))