from telegram import ReplyKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        ["Погода", "Курс валют"],
        ["Новости", "Воздушная тревога"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)