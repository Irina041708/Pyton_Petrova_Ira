from telegram import Update
from telegram.ext import CallbackContext


def log(update_csv: Update, context: CallbackContext):
    file = open('file_csv.csv', 'a', encoding="UTF-8")
    file.write(f'{update_csv.message.text}\n')
    file.close()
