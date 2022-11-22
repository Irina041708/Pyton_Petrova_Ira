from webbrowser import open_new
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy_log import *


def hi_command(update: Update, context: CallbackContext):
    
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')



def time_command(update: Update, context: CallbackContext):
    
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def calculator_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"/hi\n/time\n/calculator\n"
                "Функции калькулятора: \n"
                "1. Чтобы найти сумму, введите числа через пробел(/sum)\n"
                "2. Чтобы найти разность , введите числа через пробел(/difference)\n"
                "3. Чтобы найти произведение, введите числа через пробел(/multiplication)\n"
                "4. Чтобы найти частное, введите числа через пробел(/share)\n"
                "5. Показать Телефонный справочник из файла формата csv (/show_calculator_csv_directory)\n" 
                )


def show_calculator_csv_directory_command(update_csv: Update, context: CallbackContext):
    new_list = []
    with open("file_csv.csv", "r", encoding="utf-8") as input_read:
        new_list = input_read.read()
    update_csv.message.reply_text(f"{new_list}")


def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    print(msg)
    items = msg.split() # /sum 123 534543
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f"{x} + {y} = {x+y}")  # ~print


def difference_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    print(msg)
    items = msg.split() # /sum 123 534543
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f"{x} - {y} = {x-y}")  # ~print


def multiplication_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    print(msg)
    items = msg.split() # /sum 123 534543
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f"{x} * {y} = {x*y}")  # ~print


def share_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    print(msg)
    items = msg.split() # /sum 123 534543
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f"{x} / {y} = {x/y}")  # ~print