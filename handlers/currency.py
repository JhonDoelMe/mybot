from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.api_clients import get_currency_rate

async def currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) != 2:
        await update.message.reply_text("Используйте команду в формате: /currency [базовая валюта] [целевая валюта]")
        return
    
    base_currency, target_currency = args[0].upper(), args[1].upper()
    rate = get_currency_rate(base_currency, target_currency)
    
    if rate is None:
        await update.message.reply_text("Не удалось получить курс валюты. Проверьте коды валют и попробуйте снова.")
        return
    
    response = (
        f"Курс {base_currency} к {target_currency}:\n"
        f"1 {base_currency} = {rate} {target_currency}"
    )
    await update.message.reply_text(response)

currency_handler = CommandHandler("currency", currency)