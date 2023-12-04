import sqlite3


def find_nearest_holiday(date):
    conn = sqlite3.connect('persian holiday.sqlite3')
    cur = conn.cursor()
    cur.execute(f'select * from holiday where date = \'{date}\'')
    input_index = cur.fetchall()[0][0]

    nearest_index = input_index
    while cur.execute(f'select * from holiday where id = {nearest_index}').fetchone()[8] != 'Y':
        nearest_index += 1
    
    nearest_holiday =  cur.execute(f'select * from holiday where id = {nearest_index}').fetchone()
    print(nearest_holiday)
    return {'distance': nearest_index-input_index, 'date': nearest_holiday[1], 'info':nearest_holiday[-1]}
