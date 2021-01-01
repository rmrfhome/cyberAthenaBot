import os
import random

import settings

TOKEN = os.getenv("TELEGRAM_TOKEN")
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

delhpic_maxims = [
    "Ἕπου θεῷ",
    "Νόμῳ πείθου",
    "Θεοὺς σέβου",
    "Γονεῖς αἰδοῦ",
    "Ἡττῶ ὑπὸ δικαίου",
    "Γνῶθι μαθών",
    "Ἀκούσας νόει",
    "Σαυτὸν ἴσθι",
    "Γαμεῖν μέλλε",
    "Καιρὸν γνῶθι",
    "Φρόνει θνητά",
    "Ξένος ὢν ἴσθι",
    "Ἑστίαν τίμα",
    "Ἄρχε σεαυτοῦ",
    "Φίλοις βοήθει",
    "Θυμοῦ κράτει",
    "Φρόνησιν ἄσκει",
    "Πρόνοιαν τίμα",
    "Ὅρκῳ μὴ χρῶ",
    "Φιλίαν ἀγάπα",
    "Παιδείας ἀντέχου",
    "Δόξαν δίωκε",
    "Σοφίαν ζήλου",
    "Καλὸν εὖ λέγε",
    "Ψέγε μηδένα",
    "Ἐπαίνει ἀρετήν",
    "Πρᾶττε δίκαια",
    "Φίλοις εὐνόει",
    "Ἐχθροὺς ἀμύνου",
    "Εὐγένειαν ἄσκει",
    "Κακίας ἀπέχου",
    "Κοινὸς γίνου",
    "Ἴδια φύλαττε",
    "Ἀλλοτρίων ἀπέχου",
    "Ἄκουε πάντα",
    "Εὔφημος ἴσθι",
    "Φίλῳ χαρίζου",
    "Μηδὲν ἄγαν",
    "Χρόνου φείδου",
    "Ὅρα τὸ μέλλον",
    "Ὕβριν μίσει",
    "Ἱκέτας αἰδοῦ",
    "Πᾶσιν ἁρμόζου",
    "Υἱοὺς παίδευε",
    "Ἔχων χαρίζου",
    "Δόλον φοβοῦ",
    "Εὐλόγει πάντας",
    "Φιλόσοφος γίνου",
    "Ὅσια κρῖνε",
    "Γνοὺς πρᾶττε",
    "Φόνου ἀπέχου",
    "Εὔχου δυνατά",
    "Σοφοῖς χρῶ",
    "Ἦθος δοκίμαζε",
    "Λαβὼν ἀπόδος",
    "Ὑφορῶ μηδένα",
    "Τέχνῃ χρῶ",
    "Ὃ μέλλεις, δός",
    "Εὐεργεσίας τίμα",
    "Φθόνει μηδενί",
    "Φυλακῇ πρόσεχε",
    "Ἐλπίδα αἴνει",
    "Διαβολὴν μίσει",
    "Δικαίως κτῶ",
    "Ἀγαθοὺς τίμα",
    "Κριτὴν γνῶθι",
    "Γάμους κράτει",
    "Τύχην νόμιζε",
    "Ἐγγύην φεῦγε",
    "Ἁπλῶς διαλέγου",
    "Ὁμοίοις χρῶ",
    "Δαπανῶν ἄρχου",
    "Κτώμενος ἥδου",
    "Αἰσχύνην σέβου",
    "Χάριν ἐκτέλει",
    "Εὐτυχίαν εὔχου",
    "Τύχην στέργε",
    "Ἀκούων ὅρα",
    "Ἐργάζου κτητά",
    "Ἔριν μίσει",
    "Ὄνειδος ἔχθαιρε",
    "Γλῶτταν ἴσχε",
    "Ὕβριν ἀμύνου",
    "Κρῖνε δίκαια",
    "Χρῶ χρήμασιν",
    "Ἀδωροδόκητος δίκαζε",
    "Αἰτιῶ παρόντα",
    "Λέγε εἰδώς",
    "Βίας μὴ ἔχου",
    "Ἀλύπως βίου",
    "Ὁμίλει πρᾴως",
    "Πέρας ἐπιτέλει μὴ ἀποδειλιῶν",
    "Φιλοφρόνει πᾶσιν",
    "Υἱοῖς μὴ καταρῶ",
    "Γυναικὸς ἄρχε",
    "Σεαυτὸν εὖ ποίει",
    "Εὐπροσήγορος γίνου",
    "Ἀποκρίνου ἐν καιρῷ",
    "Πόνει μετ’ εὐκλείας",
    "Πρᾶττε ἀμετανοήτως",
    "Ἁμαρτάνων μετανόει",
    "Ὀφθαλμοῦ κράτει",
    "Βουλεύου χρόνῳ",
    "Πρᾶττε συντόμως",
    "Φιλίαν φύλαττε",
    "Εὐγνώμων γίνου",
    "Ὁμόνοιαν δίωκε",
    "Ἄρρητον κρύπτε",
    "Τὸ κρατοῦν φοβοῦ",
    "Τὸ συμφέρον θηρῶ",
    "Καιρὸν προσδέχου",
    "Ἔχθρας διάλυε",
    "Γῆρας προσδέχου",
    "Ἐπὶ ῥώμῃ μὴ καυχῶ",
    "Εὐφημίαν ἄσκει",
    "Ἀπέχθειαν φεῦγε",
    "Πλούτει δικαίως",
    "Δόξαν μὴ λεῖπε",
    "Κακίαν μίσει",
    "Κινδύνευε φρονίμως",
    "Μανθάνων μὴ κάμνε",
    "Φειδόμενος μὴ λεῖπε",
    "Χρησμοὺς θαύμαζε",
    "Οὓς τρέφεις, ἀγάπα",
    "Ἀπόντι μὴ μάχου",
    "Πρεσβύτερον αἰδοῦ",
    "Νεώτερον δίδασκε",
    "Πλούτῳ ἀπίστει",
    "Σεαυτὸν αἰδοῦ",
    "Μὴ ἄρχε ὑβρίζειν",
    "Προγόνους στεφάνου",
    "Θνῆσκε ὑπὲρ πατρίδος",
    "Τῷ βίῳ μὴ ἄχθου",
    "Ἐπὶ νεκρῷ μὴ γέλα",
    "Ἀτυχοῦντι συνάχθου",
    "Χαρίζου ἀβλαβῶς",
    "Μὴ ἐπὶ παντὶ λυποῦ",
    "Ἐξ εὐγενῶν γέννα",
    "Ἐπαγγέλλου μηδενί",
    "Φθιμένους μὴ ἀδίκει",
    "Εὖ πάσχε ὡς θνητός",
    "Τύχῃ μὴ πίστευε",
    "Παῖς ὢν κόσμιος ἴσθι",
    "Ἡβῶν ἐγκρατής",
    "Μέσος δίκαιος",
    "Πρεσβύτης εὔλογος",
    "Τελευτῶν ἄλυπος",
]

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
# def start(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /start is issued."""
#     update.message.reply_text('Hi!')

def advice(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text(random.choice(delhpic_maxims))


# def help_command(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /help is issued."""
#     update.message.reply_text('Help!')


# def echo(update: Update, context: CallbackContext) -> None:
#     """Echo the user message."""
#     update.message.reply_text(update.message.text)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    #dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("advice", advice))
    #dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()