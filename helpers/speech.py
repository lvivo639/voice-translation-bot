import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from pydub import AudioSegment
from google.oauth2 import service_account


def ogg_to_wav(audio_file_name):
    fn = audio_file_name.split('.')
    if fn[1] == 'ogg':
        sound = AudioSegment.from_ogg(audio_file_name)
        audio_file_name = fn[0] + '.flac'
        sound.export(audio_file_name, format="flac")
        return audio_file_name


def speech_to_text(ogg_file_name, lang='ru-RU'):
    flac_file_name = ogg_to_wav(ogg_file_name)
    google_config_path = os.getenv("GOOGLE_CONFIG_PATH")
    credentials = service_account.Credentials.from_service_account_file(google_config_path)
    client = speech.SpeechClient(credentials=credentials)

    with io.open(flac_file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config_p = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=48000,
        language_code=lang,
    )

    # Detects speech in the audio file
    response = client.recognize(config_p, audio)
    res = response.results
    if len(res):
        alt = res[0].alternatives
        if len(alt):
            trans = alt[0].transcript
            return trans
    return "Говорите чётко, пожалуйста"



