from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("Погода", callback_data="Погода"),
         InlineKeyboardButton("Курс валют", callback_data="Курс валют")],
        [InlineKeyboardButton("Новости", callback_data="Новости"),
         InlineKeyboardButton("Воздушная тревога", callback_data="Воздушная тревога")]
    ]
    return InlineKeyboardMarkup(keyboard)