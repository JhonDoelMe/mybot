from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from utils.api_clients import get_latest_news

def news(update: Update, context: CallbackContext):
    articles = get_latest_news()
    
    if not articles:
        update.message.reply_text("Не удалось получить новости. Попробуйте позже.")
        return
    
    response = "Последние новости:\n"
    for i, article in enumerate(articles[:5], start=1):  # Показываем только первые 5 новостей
        title = article.get("title", "Нет заголовка")
        description = article.get("description", "Нет описания")
        response += f"{i}. {title}\n{description}\n\n"
    
    update.message.reply_text(response)

news_handler = CommandHandler("news", news)