import psycopg2
import os

_DB_CONFIG = {
    'host': os.getenv("DB_HOST"),
    'port': os.getenv("5432"),
    'database': os.getenv("startupbot"),
    'user': os.getenv("postgres"),
    'password': os.getenv("qwerty")
}

conn = psycopg2.connect(**_DB_CONFIG)

_cur = conn.cursor()
_script_dir = os.path.dirname(__file__)

with open(os.path.join(_script_dir, 'create.sql'), 'r+') as f:
    q = f.read()

_cur.execute(q)
conn.commit()
_cur.close()
