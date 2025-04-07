from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from utils.keyboards import main_menu_keyboard

def start(update: Update, context: CallbackContext):
    keyboard = main_menu_keyboard()
    update.message.reply_text("Привет! Выбери нужный раздел:", reply_markup=keyboard)

start_handler = CommandHandler('start', start)