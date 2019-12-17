import telebot
from commands.start import com_start_message
from commands.type_voice import com_get_voice
from commands.type_text import com_type_text
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

com_start_message(bot)
com_get_voice(bot, TOKEN)
com_type_text(bot)

print('Bot pooling')
bot.polling()
