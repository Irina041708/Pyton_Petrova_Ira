from telegram import Update
from telegram.ext import Updater, CommandHandler
from bot_commands import *

updater = Updater('Вставьте пожалуйста свой токен:)))')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('telephone_directory', telephone_directory_command))
updater.dispatcher.add_handler(CommandHandler('show_phone_directory', show_phone_directory_command))
updater.dispatcher.add_handler(CommandHandler('add_key', add_key_command))
updater.dispatcher.add_handler(CommandHandler('add_key_csv', add_key_csv_command))
updater.dispatcher.add_handler(CommandHandler('show_phone_csv_directory', show_phone_csv_directory_command))
updater.start_polling() #запускает наш бот на постоянную обработку  
updater.idle()
