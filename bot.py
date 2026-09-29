
import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "👋 أهلاً بك في بوت العب واربح!\n\n"
        "🎮 هنا ستجد عروض وألعاب يمكنك تنفيذها للحصول على مكافآت.\n\n"
        "اختر من العروض المتاحة وابدأ اللعب."
    )

@bot.message_handler(commands=["offers"])
def offers(message):
    bot.reply_to(
        message,
        "🎮 العروض المتاحة حالياً:\n\n"
        "سيتم إضافة العروض هنا قريباً."
    )

@bot.message_handler(func=lambda message: True)
def welcome(message):
    bot.reply_to(
        message,
        "استخدم /start للبدء أو /offers لرؤية العروض."
    )

print("Bot is running...")

bot.infinity_polling()
