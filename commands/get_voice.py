import requests, json
from helper.speech import speech_to_text


def com_get_voice(bot, TOKEN):
    @bot.message_handler(content_types=['voice'])
    def handle_docs_audio(message):
        file_id = message.voice.file_id
        file_info = bot.get_file(file_id)
        url = 'https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path)
        file = requests.get(url)
        file_name = 'tmp/voice.ogg'
        with open(file_name, 'wb') as f:
            f.write(file.content)
        text = speech_to_text(file_name)

        bot.send_message(message.chat.id, text)
