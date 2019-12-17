import requests, json
from helpers.speech import speech_to_text
from models.tg_user import TgUserModel
from helpers.translate import translate


def com_get_voice(bot, TOKEN):
    @bot.message_handler(content_types=['voice'])
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
                file_id = message.voice.file_id
                file_info = bot.get_file(file_id)
                url = 'https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path)
                file = requests.get(url)
                file_name = 'tmp/voice.ogg'
                with open(file_name, 'wb') as f:
                    f.write(file.content)
                text = speech_to_text(file_name)

                user_lang = TgUserModel.get_user(user_id)["lang"]
                target = 'ru' if user_lang == 'en' else 'en'
                translated_text = translate(text, target)
                reply_text = f'Распознаный текст:\n{text}\n--\nПеревод:\n{translated_text}'
                bot.reply_to(message, reply_text)
