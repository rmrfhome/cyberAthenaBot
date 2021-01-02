from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, Updater, CallbackContext, CommandHandler, CallbackQueryHandler
import random
import bot.const as const
import grammar.latin as latin
import grammar.greek as greek


def __advice(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(const.delhpic_maxims))


def __start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Χαῖρε!")


def __latin(update: Update, context: CallbackContext) -> None:
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

# ἀλήθεια, -ας, ἡ
# βασιλεία, -ας, ἡ
# Γαλιλαία, -ας, ἡ
# ἐκκλησία, -ας, ἡ
# ἐπαγγελία, -ας, ἡ
# καρδία, -ας, ἡ
# ὥρα, -ας, ἡ
# ἀλήθεια, -ας, ἡ
# ἀλήθεια, -ας, ἡ
def __greek(update: Update, context: CallbackContext) -> None:
    def create_noun(stem: str) -> greek.Noun:
        return greek.Noun(stem, "ας", greek.Declension.First, greek.Gender.Female)
    stems = [
        'ἀλήθει',
        'βασιλει',
        'Γαλιλαι',
        'ἐκκλησι',
        'ἐπαγγελι',
        'καρδι',
        'ὥρ',
        'ἀληθει',
        'ἀληθει',
    ]
    nouns = list(map(create_noun, stems))
    question = greek.create_question(random.choice(nouns))
    kl = list(map(lambda x: InlineKeyboardButton(x.value, callback_data='Пральн!' if x.isValid else 'Нет!'), question.answers))
    keyboard = [
        [kl[0], kl[1]],
        [kl[2], kl[3]]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(question.question, reply_markup=reply_markup)


def __button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer(text=query.data)


def register(dispatcher : Dispatcher):
    handlers = {
        'start': __start,
        'advice': __advice,
        'latin': __latin,
        'greek': __greek,
    }
    for key, value in handlers.items():
        dispatcher.add_handler(CommandHandler(key, value))
    dispatcher.add_handler(CallbackQueryHandler(__button))