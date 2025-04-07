from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.api_clients import get_air_0raid_status

async def air_raid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status = get_air_raid_status()
    
    if status is None:
        await update.message.reply_text("Не удалось получить информацию о воздушной тревоге. Попробуйте позже.")
        return
    
    if not status:
        await update.message.reply_text("Воздушная тревога не объявлена.")
        return
    
    response = "Активные зоны воздушной тревоги:\n"
    for alert in status:
        region = alert.get("region", "Неизвестный регион")
        level = alert.get("level", "Неизвестный уровень")
        response += f"Регион: {region}, Уровень: {level}\n"
    
    await update.message.reply_text(response)

air_raid_handler = CommandHandler("air_raid", air_raid)