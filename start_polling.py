from dotenv import load_dotenv
import os
import sys
from telegram.ext import Updater

sys.path.insert(0, "azure_function")
import athena_bot.bot as athena_bot
import athena_bot.latin as latin

load_dotenv(verbose=True)
TOKEN = os.getenv("TELEGRAM_TOKEN")

def main():
    updater = Updater(TOKEN, use_context=True)
    athena_bot.register_command_handlers(updater.dispatcher)
    updater.start_polling()
    updater.idle()
    # print(latin.conjugate(verbi[0], latin.Numerus.Singularis, latin.Casus.Ablativus))
    # print(latin.conjugate(verbi[0], latin.Numerus.Pluralis, latin.Casus.Ablativus))
    # print(verbi[0])
    #print()




if __name__ == '__main__':
    main()