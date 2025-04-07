from telegram.ext import Updater, Dispatcher
from handlers.start import start_handler
from handlers.weather import weather_handler
from handlers.currency import currency_handler
from handlers.news import news_handler
from handlers.air_raid import air_raid_handler
from config import TOKEN

def main():
    updater = Updater(TOKEN)
    dispatcher: Dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(weather_handler)
    dispatcher.add_handler(currency_handler)
    dispatcher.add_handler(news_handler)
    dispatcher.add_handler(air_raid_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()