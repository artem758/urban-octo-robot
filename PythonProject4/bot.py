# Убедись, что у тебя установлена библиотека:
# pip install python-telegram-bot

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters
)

from elvirix_llm import elvirix_generate

# 🔐 Токен Telegram-бота — держи в секрете
API_TOKEN = "7682147582:AAFwpGeDlY7--CFgHa6tnqAWzOADi4zhNvU"

# 🎯 Функция обработки входящих сообщений
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    response = elvirix_generate(user_text)
    await update.message.reply_text(response)

# 🚀 Запуск бота
def main():
    app = ApplicationBuilder().token(API_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()

if __name__ == "__main__":
    main()