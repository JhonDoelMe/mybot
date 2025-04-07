from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from utils.api_clients import get_air_raid_status

def air_raid(update: Update, context: CallbackContext):
    status = get_air_raid_status()
    
    if status is None:
        update.message.reply_text("Не удалось получить информацию о воздушной тревоге. Попробуйте позже.")
        return
    
    if not status:
        update.message.reply_text("Воздушная тревога не объявлена.")
        return
    
    response = "Активные зоны воздушной тревоги:\n"
    for alert in status:
        region = alert.get("region", "Неизвестный регион")
        level = alert.get("level", "Неизвестный уровень")
        response += f"Регион: {region}, Уровень: {level}\n"
    
    update.message.reply_text(response)

air_raid_handler = CommandHandler("air_raid", air_raid)