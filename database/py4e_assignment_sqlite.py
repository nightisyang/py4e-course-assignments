import sqlite3
import re


conn = sqlite3.connect('count_org.sqlite')
cur = conn.cursor()

# DROP - delete database if it exist
cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')

if (len(fname) < 1):
    fname = 'mbox.txt'

fh = open(fname)
# print(fh.read())

for line in fh:
    line = line.rstrip()
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    # print(email)
    domain = email.split('@')[1]
    # if len(domain) > 1:
    print(domain)

    # opening a set of records - like a cursor ? = placeholder (email,) = tupple
    cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))

    # grab the first one
    row = cur.fetchone()

    # if there is no rows, no data
    if row is None:

        # insert into the first row
        cur.execute(
            '''INSERT INTO Counts (org, count) VALUES (?, 1)''', (domain,))

    # if there is a row
    else:
        cur.execute(
            'UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(row[0], row[1])

cur.close()
