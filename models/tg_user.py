from psycopg2.extras import DictCursor


class TgUser:
    def __init__(self, bd_id, tg_id, language):
        self.bd_id = bd_id
        self.tg_id = tg_id
        self.language = language


class TgUserModel:
    def __init__(self, conn):
        self._conn = conn
        self._cur = conn.cursor(cursor_factory=DictCursor)

    def insert(self, tg_id, language='ru-RU'):
        q = 'INSERT INTO tg_user (tg_id, language) VALUES (%s, %s) RETURNING db_id'
        res = self._cur.execute(q, (tg_id, language,))
        self._conn.commit()
        return res

    def is_user(self, tg_id):
        q = 'SELECT * FROM tg_user WHERE tg_id = %s'
        res = self._cur.execute(q, (tg_id,))
        return res

    def get_lang(self, tg_id):
        q = 'SELECT tg_user.language FROM tg_user WHERE tg_id = %s'
        res = self._cur.execute(q, (tg_id,))
        return res