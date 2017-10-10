import sqlite3


def connect():
    c = sqlite3.connect('books.db')
    cur = c.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT,'
                'author TEXT, year INTEGER, isbn INTEGER)')
    c.commit()
    c.close()


def insert(title, author, year, isbn):
    c = sqlite3.connect('books.db')
    cur = c.cursor()
    cur.execute('INSERT INTO book VALUES(NULL, ?, ?, ?, ?)', (title, author, year, isbn))
    c.commit()
    c.close()


def view():
    c = sqlite3.connect('books.db')
    cur = c.cursor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()
    c.close()
    return rows


def search(title='', author='', year='', isbn=''):
    c = sqlite3.connect('books.db')
    cur = c.cursor()
    cur.execute('SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
    rows = cur.fetchall()
    c.close()
    return rows


def delete(id):
    c = sqlite3.connect('books.db')
    cur = c.cursor()
    cur.execute('DELETE FROM book WHERE id=?', (id,))
    c.commit()
    c.close()


def update(id, title, author, year, isbn):
    c = sqlite3.connect('books.db')
    cur = c.cursor()
    cur.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))
    c.commit()
    c.close()


connect()
# insert(title='The Earth', author='John Smith', year=1918, isbn=994123492)
# print(view())
# delete(3)
# update(4, 'The Earth 2', 'John Smith', 1918, 994123492)
# print(view())
# print(search(author='John Tablet'))
