CREATE TABLE IF NOT EXISTS tg_user
(
    db_id      serial PRIMARY KEY,
    tg_id int NOT NULL,
    language varchar(12) NOT NULL DEFAULT 'ru-RU'
);