import sqlite3 as sl
import sys

con = sl.connect('my-test.db')

with con:
    data = con.execute("SELECT * FROM WORDS WHERE count > 200 ORDER BY count")
    for row in data:
        print(row)
    print('-----------------------------')
    data = con.execute("SELECT * FROM WORDS WHERE count > 200 ORDER BY word")
    for row in data:
        print(row)