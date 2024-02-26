import sqlite3 as sq


def sql_start(connectionString):
    global base, cur
    base = sq.connect(connectionString)
    cur = base.cursor()
    if base:
        print('Database is connected')
    base.execute(
        'CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, decription TEXT, price TEXT)')
    base.commit()

    return base


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)',
                    tuple(data.values()))
        base.commit()


async def sql_read(message, bot):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
