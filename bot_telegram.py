from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin
from data_base import sqlite_db

connectionString = 'tour.db'

async def on_startup(_):
    print('Бот в сети')
    sqlite_db.sql_start(connectionString)

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
