from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.api_clients import get_weather

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = " ".join(context.args) if context.args else "Kyiv"  # По умолчанию Киев
    data = get_weather(city)
    
    if data.get("cod") != 200:
        await update.message.reply_text("Город не найден. Попробуйте еще раз.")
        return
    
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    
    response = (
        f"Погода в городе {city.capitalize()}:\n"
        f"Описание: {weather_description}\n"
        f"Температура: {temperature}°C\n"
        f"Влажность: {humidity}%"
    )
    await update.message.reply_text(response)

weather_handler = CommandHandler("weather", weather)