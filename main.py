from telebot import TeleBot


bot = TeleBot("7903097791:AAGUPnjfkkBDmrdhuQpObtKi5gIz66LkP2g")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum!")









bot.polling()