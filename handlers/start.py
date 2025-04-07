from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.keyboards import main_menu_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = main_menu_keyboard()
    await update.message.reply_text("Привет! Выбери нужный раздел:", reply_markup=keyboard)

start_handler = CommandHandler('start', start)