from models.tg_user import TgUserModel
from helpers.translate import translate


def com_type_text(bot):
    @bot.message_handler(content_types=['text'])
    def handle_docs_audio(message):
        if message.chat.type == 'private':
            chat_id = message.chat.id
            if not TgUserModel.get_user(chat_id):
                bot.reply_to(message, 'Нажмите /start')
            else:
                bot.reply_to(message, 'Используйте бота в беседе со своим иностранным собеседником')
        else:
            user_id = message.from_user.id
            if not TgUserModel.get_user(user_id):
                bot.reply_to(message, "Выберите язык в настройках бота через личные сообщения, пожалуйста")
            else:
                text = message.text
                user_lang = TgUserModel.get_user(user_id)["lang"]
                target = 'ru' if user_lang == 'en' else 'en'
                translated_text = translate(text, target)
                bot.reply_to(message, "Перевод:\n" + translated_text)
