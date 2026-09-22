import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
        CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
    
    
)

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])
WELCOME = """☀️ BUONGIORNO FAMILY! ❤️

⭐ NUOVO CANALE ⭐

Benvenuti nella nostra community
RealWonder420 ✨

Qui troverete novità, prodotti, offerte
e tutte le nostre comunicazioni 📲

Restate con noi e non perdetevi le
prossime sorprese! 🤩🎁

Grazie di essere parte della nostra
Family! ❤️❤️❤️"""


def welcome_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📦 Prodotti", callback_data="prodotti"),
            InlineKeyboardButton("📱 Contatti", callback_data="contatti"),
        ],
        [
            InlineKeyboardButton("🧑‍🍳 Menù", callback_data="menu"),
        ],
    ])


def back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("↩️ Indietro", callback_data="home")]
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME,
        reply_markup=welcome_keyboard()
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "home":
        await query.edit_message_text(
            WELCOME,
            reply_markup=welcome_keyboard()
        )

    elif query.data == "prodotti":
        text = """📦 Prodotti

Disponibile ✅
D Premium 🇪🇸⭐️

In Arrivo ⏳
🥶 Frozen-Static 🧊"""
        await query.edit_message_text(
            text,
            reply_markup=back_keyboard()
        )

    elif query.data == "contatti":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(
                "📷 Profilo Instagram",
                url="https://www.instagram.com/wonderfarm420real?stkn=MTV6ZHJtbGFlMDh1MQ%3D%3D&utm_source=qr"
            )],
            [InlineKeyboardButton(
                "✈️ Contatto Telegram",
                url="https://t.me/RealWonder2026"
            )],
            [InlineKeyboardButton(
                "💬 Contatto WhatsApp",
                url="https://wa.me/393319534771"
            )],
            [InlineKeyboardButton(
                "↩️ Indietro",
                callback_data="home"
            )],
        ])

        await query.edit_message_text(
            "📱 Contatti",
            reply_markup=keyboard
        )

    elif query.data == "menu":
        await query.edit_message_text(
            """🧑‍🍳 Menù

⏳⏳⏳""",
            reply_markup=back_keyboard()
        )
        


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.run_polling()


if __name__ == "__main__":
    main()
