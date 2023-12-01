import sqlite3 as sql
import random

def isholiday(date):
    print(date)
    con = sql.connect("persian holiday 02.db")
    # cur = con.cursor()
    # ans = (cur.execute("select * from Holiday where date == '" + date+ "\'").fetchall()[0][7])
    # return True if ans else False

# date = "1402-01-04"
# print("select * from Holiday where date == " + date)
# print(isholiday(date)[0][7])
