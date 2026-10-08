import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🎁 Bonus", "🎟 Promo kod"],
        ["🔗 Havola", "📞 Yordam"],
        ["📢 Yangiliklar"]
    ]

    markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🇺🇿 Assalomu alaykum!\n\nKerakli bo‘limni tanlang 👇",
        reply_markup=markup
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🎁 Bonus":
        await update.message.reply_text("🎁 Bonus bo‘limi tez orada ishga tushadi.")

    elif text == "🎟 Promo kod":
        await update.message.reply_text("🎟 Promo kod: TEZ_ORADA")

    elif text == "🔗 Havola":
        await update.message.reply_text("🔗 Hamkorlik havolasi tez orada qo‘shiladi.")

    elif text == "📞 Yordam":
        await update.message.reply_text("📞 Yordam uchun administratorga murojaat qiling.")

    elif text == "📢 Yangiliklar":
        await update.message.reply_text("📢 Yangiliklar tez orada shu yerda.")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
