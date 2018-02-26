import sqlite3


class Database:
    def __init__(self):
        self.c = sqlite3.connect('books.db')
        self.cur = self.c.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, '
                         'author TEXT, year INTEGER, isbn INTEGER)')
        self.c.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute('INSERT INTO book VALUES(NULL, ?, ?, ?, ?)', (title, author, year, isbn))
        self.c.commit()

    def view(self):
        self.cur.execute('SELECT * FROM book')
        rows = self.cur.fetchall()
        return rows

    def search(self, title='', author='', year='', isbn=''):
        self.cur.execute('SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute('DELETE FROM book WHERE id=?', (id,))
        self.c.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))
        self.c.commit()

    def __del__(self):
        self.c.close()

# connect()
# insert(title='The Earth', author='John Smith', year=1918, isbn=994123492)
# print(view())
# delete(3)
# update(4, 'The Earth 2', 'John Smith', 1918, 994123492)
# print(view())
# print(search(author='John Tablet'))
