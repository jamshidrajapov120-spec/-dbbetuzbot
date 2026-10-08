import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🎁 Bonus", "🎟 Promo kod"],
        ["🔗 Havola", "📞 Yordam"],
        ["📢 Yangiliklar"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🇺🇿 Assalomu alaykum!\n\nKerakli bo‘limni tanlang 👇",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
