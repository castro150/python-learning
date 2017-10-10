import sqlite3


def create_table():
    c = sqlite3.connect('lite.db')
    cur = c.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    c.commit()
    c.close()


def insert(item, quantity, price):
    c = sqlite3.connect('lite.db')
    cur = c.cursor()
    cur.execute('INSERT INTO store VALUES(?, ?, ?)', (item, quantity, price))
    c.commit()
    c.close()


def view():
    c = sqlite3.connect('lite.db')
    cur = c.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    c.close()
    return rows


def delete(item):
    c = sqlite3.connect('lite.db')
    cur = c.cursor()
    cur.execute('DELETE FROM store WHERE item=?', (item,))
    c.commit()
    c.close()


def update(quantity, price, item):
    c = sqlite3.connect('lite.db')
    cur = c.cursor()
    cur.execute('UPDATE store SET quantity=?, price=? WHERE item=?', (quantity, price, item))
    c.commit()
    c.close()


print(view())
#insert('Coffee Cup', 10, 5)
#delete('Coffee Cup')
update(11, 15.6, 'Water Glass')
print(view())
