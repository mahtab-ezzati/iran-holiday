import sqlite3


def find_nearest_holiday(date):
    conn = sqlite3.connect('persian holiday 04.db')
    cur = conn.cursor()
    cur.execute(f'select * from holiday where date = \'{date}\'')
    index = cur.fetchall()[0][0]

    while cur.execute(f'select * from holiday where id = {index}').fetchone()[7] != 'Y':
        index += 1

    nearest_holiday =  cur.execute(f'select * from holiday where id = {index}').fetchone()
    return f'{nearest_holiday[1]} {nearest_holiday[6]}'
