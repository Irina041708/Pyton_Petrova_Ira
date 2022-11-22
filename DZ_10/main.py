from telegram import Update
from telegram.ext import Updater, CommandHandler
from bot_commands import *

updater = Updater('5746952259:AAG-HBZWgiWusC24uo3wDBl2kjhHmtpZTJc')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('calculator', calculator_command))

updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('difference', difference_command))
updater.dispatcher.add_handler(CommandHandler('multiplication', multiplication_command))
updater.dispatcher.add_handler(CommandHandler('share', share_command))

updater.dispatcher.add_handler(CommandHandler('show_calculator_csv_directory', show_calculator_csv_directory_command))
updater.start_polling() #запускает наш бот на постоянную обработку  
updater.idle()
