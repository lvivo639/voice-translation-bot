from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


class TgUser:
    def __init__(self, bd_id, tg_id, language):
        self.bd_id = bd_id
        self.tg_id = tg_id
        self.language = language


class __TgUserModel:
    def __init__(self):
        client = MongoClient(os.getenv("MONGO_DB"))
        db = client["startup"]
        self.table = db["tguser"]

    def insert(self, tg_id, lang):
        if bool(self.get_user(tg_id)):
            return None
        self.table.insert_one({"tg_id": tg_id, "lang": lang})

    def get_user(self, tg_id):
        return self.table.find_one({"tg_id": tg_id})


TgUserModel = __TgUserModel()
