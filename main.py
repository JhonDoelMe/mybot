from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.start import start_handler
from handlers.weather import weather_handler
from handlers.currency import currency_handler
from handlers.news import news_handler
from handlers.air_raid import air_raid_handler
from config import TOKEN

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Register handlers
    application.add_handler(start_handler)
    application.add_handler(weather_handler)
    application.add_handler(currency_handler)
    application.add_handler(news_handler)
    application.add_handler(air_raid_handler)

    application.run_polling()

if __name__ == '__main__':
    main()