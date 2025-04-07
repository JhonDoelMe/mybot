from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes
from utils.api_clients import get_air_raid_status, get_currency_rate, get_latest_news
from utils.weather import get_weather  # type: ignore # Import the get_weather function
from utils.keyboards import main_menu_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = main_menu_keyboard()
    await update.message.reply_text("Привет! Выбери нужный раздел:", reply_markup=keyboard)

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "Погода":
        await weather(update, context)
    elif query.data == "Курс валют":
        await currency(update, context)
    elif query.data == "Новости":
        await news(update, context)
    elif query.data == "Воздушная тревога":
        await air_raid(update, context)

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = "Kyiv"  # По умолчанию Киев
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

async def currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    base_currency = "USD"
    target_currency = "UAH"
    rate = get_currency_rate(base_currency, target_currency)
    
    if rate is None:
        await update.message.reply_text("Не удалось получить курс валюты. Проверьте коды валют и попробуйте снова.")
        return
    
    response = (
        f"Курс {base_currency} к {target_currency}:\n"
        f"1 {base_currency} = {rate} {target_currency}"
    )
    await update.message.reply_text(response)

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    articles = get_latest_news()
    
    if not articles:
        await update.message.reply_text("Не удалось получить новости. Попробуйте позже.")
        return
    
    response = "Последние новости:\n"
    for i, article in enumerate(articles[:5], start=1):  # Показываем только первые 5 новостей
        title = article.get("title", "Нет заголовка")
        description = article.get("description", "Нет описания")
        response += f"{i}. {title}\n{description}\n\n"
    
    await update.message.reply_text(response)

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

start_handler = CommandHandler('start', start)
button_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_button)