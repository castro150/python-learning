import psycopg2


def create_table():
    c = psycopg2.connect('dbname=\'database1\' user=\'postgres\' password=\'postgres123\' '
                         'host=\'localhost\' port=\'5432\'')
    cur = c.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    c.commit()
    c.close()


def insert(item, quantity, price):
    c = psycopg2.connect('dbname=\'database1\' user=\'postgres\' password=\'postgres123\' '
                         'host=\'localhost\' port=\'5432\'')
    cur = c.cursor()
    cur.execute('INSERT INTO store VALUES(%s, %s, %s)', (item, quantity, price))
    c.commit()
    c.close()


def view():
    c = psycopg2.connect('dbname=\'database1\' user=\'postgres\' password=\'postgres123\' '
                         'host=\'localhost\' port=\'5432\'')
    cur = c.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    c.close()
    return rows


def delete(item):
    c = psycopg2.connect('dbname=\'database1\' user=\'postgres\' password=\'postgres123\' '
                         'host=\'localhost\' port=\'5432\'')
    cur = c.cursor()
    cur.execute('DELETE FROM store WHERE item=%s', (item,))
    c.commit()
    c.close()


def update(quantity, price, item):
    c = psycopg2.connect('dbname=\'database1\' user=\'postgres\' password=\'postgres123\' '
                         'host=\'localhost\' port=\'5432\'')
    cur = c.cursor()
    cur.execute('UPDATE store SET quantity=%s, price=%s WHERE item=%s', (quantity, price, item))
    c.commit()
    c.close()


print(view())
#insert('Coffee Cup', 10, 5)
#delete('Coffee Cup')
update(11, 15.6, 'Water Glass')
print(view())
