from telebot import types
from models.tg_user import TgUserModel


def language_keyboard(back=None):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add('English', 'Русский')
    if back:
        markup.add('Назад')
    return markup


def remove_keyboard():
    return types.ReplyKeyboardRemove()


def com_start_message(bot):
    @bot.message_handler(commands=['start'])
    def f(message):
        chat_id = message.chat.id
        if message.chat.type == 'private':
            if not TgUserModel.get_user(chat_id):
                markup = language_keyboard()
                msg = bot.send_message(chat_id, "Привет, я ваш личный бот переводчик.\nВыберите свой родной язык",
                                       reply_markup=markup)
                bot.register_next_step_handler(msg, process_language_step)
            else:
                bot.send_message(chat_id, 'Нажмите /language, чтобы изменить настройки языка')
        else:
            bot.reply_to(message, 'Для личных натроек перейдите в личную переписку с ботом')

    def process_language_step(message):
        language = message.text
        chat_id = message.chat.id
        if language == 'English':
            TgUserModel.insert(chat_id, 'en')
            bot.send_message(chat_id, f"Language selected: {language}", reply_markup=remove_keyboard())
        elif language == 'Русский':
            TgUserModel.insert(chat_id, 'ru')
            bot.send_message(chat_id, f"Язык выбран: {language}", reply_markup=remove_keyboard())
        else:
            markup = language_keyboard()
            msg = bot.send_message(chat_id, "Выберите один из языков",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, process_language_step)

    return f


