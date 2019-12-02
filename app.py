import telebot
from commands.start import com_start_message
from commands.get_voice import com_get_voice
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

com_start_message(bot)
com_get_voice(bot, TOKEN)

print('Bot pooling')
bot.polling()
