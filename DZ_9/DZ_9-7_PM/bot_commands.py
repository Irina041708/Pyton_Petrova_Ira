from webbrowser import open_new
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
import jf
from spy_log import *


def hi_command(update: Update, context: CallbackContext):
    
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')



def time_command(update: Update, context: CallbackContext):
    
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def telephone_directory_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"/hi\n/time\n/telephone_directory\n"
                "Телефонный справочник: \n"
                "1. Показать Телефонный справочник из файла формата json (/show_phone_directory)\n"
                "2. Ввод данных: Фамилия Имя Телефон через пробел и сохранение в файле формата json (/add_key)\n"
                "3. Показать Телефонный справочник из файла формата csv (/show_phone_csv_directory)\n" 
                "4. Ввод данных: Фамилия Имя Телефон через пробел и сохранение в файле формата csv (/add_key_csv)\n" 
                 )


def show_phone_directory_command(update: Update, context: CallbackContext):
    new_list = []
    with open("data_file.json", "r", encoding="utf-8") as input_read:
        new_list = input_read.read()
    update.message.reply_text(f'{new_list}')   


def show_phone_csv_directory_command(update_csv: Update, context: CallbackContext):
    new_list = []
    with open("file_csv.csv", "r", encoding="utf-8") as input_read:
        new_list = input_read.read()
    update_csv.message.reply_text(f'{new_list}')


def add_key_command(update: Update, context: CallbackContext):
    file = "data_file.json"
    msg = update.message.text.split(" ")
    if len(msg) == 4:
        if len(msg[1])!=0 and len(msg[2])!=0 and len(msg[3])!=0:
            jf.append_to_json(file,msg[1:])
            update.message.reply_text(f"Данные добавлены {msg[1]}  {msg[2]}  {msg[3]}\n")
            return
    update.message.reply_text("Введены неправильные данные")


def add_key_csv_command(update_csv: Update, context: CallbackContext):
    log(update_csv, context)
    msg = update_csv.message.text.split()
    if len(msg) == 4:
        if len(msg[1])!=0 and len(msg[2])!=0 and len(msg[3])!=0:
            update_csv.message.reply_text(f"Данные добавлены {msg[1]}  {msg[2]}  {msg[3]}\n")
            return
    update_csv.message.reply_text("Введены неправильные данные")
    