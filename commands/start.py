
def com_start_message(bot):
    @bot.message_handler(commands=['start'])
    def f(message):
        bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    return f
