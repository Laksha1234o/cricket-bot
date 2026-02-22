import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("8495068953:AAG78mUG-Z0CgYGHe0pLNPt1HMHN1ctPByw")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📥 Get Cricket App", callback_data="get_app")],
        [InlineKeyboardButton("📜 Instructions", callback_data="instructions")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🏏 *Welcome to Online Cricket Match Watcher Bot*\n"
        "✨ _(Made by CUS0469)_\n\n"
        "Please choose an option below:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "get_app":
        await query.edit_message_text(
            "📥 *Download Cricket App*\n\n"
            "Click the link below to download the app:\n"
            "🔗 https://filmm.me/SyfNVrge",
            parse_mode="Markdown"
        )

    elif query.data == "instructions":
        await query.edit_message_text(
            "📜 *Instructions to Watch Matches*\n\n"
            "1️⃣ Download the app from the given link otherwise the matches will not be shown for free.\n\n"
            "2️⃣ Signup in the app to watch all the matches.\n\n"
            "3️⃣ 🎉 You are good to go!",
            parse_mode="Markdown"
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
