import sqlite3


CREATE_STOCK_TABLE = '''CREATE TABLE IF NOT EXISTS stock 
(name TEXT PRIMARY KEY, category TEXT, cost TEXT, amount INTEGER, manufacturer TEXT, 
FOREIGN KEY (manufacturer) REFERENCES manufacturers(manufacturer));'''

CREATE_MANUFACTURER_TABLE = '''CREATE TABLE IF NOT EXISTS manufacturers
(manufacturer TEXT PRIMARY KEY, address TEXT, delivery_day TEXT, 
FOREIGN KEY (delivery_day) REFERENCES deliveries(delivery_day));'''


CREATE_DELIVERY_TABLE = '''CREATE TABLE IF NOT EXISTS deliveries 
(delivery_day TEXT PRIMARY KEY, phone_number TEXT,
manufacturer TEXT,
delivery_person TEXT,
FOREIGN KEY (manufacturer) REFERENCES manufacturers(manufacturer));'''

INSERT_ITEM = "INSERT INTO stock(name, category, cost, amount, manufacturer) VALUES (?, ?, ?, ?, ?);"
INSERT_MANUFACTURER = "INSERT INTO manufacturers(manufacturer, address, delivery_day) VALUES (?, ?, ?);"
REMOVE_ITEM = "DELETE FROM stock WHERE name = ?;"
SEARCH_ITEM_BY_NAME = "SELECT * FROM stock WHERE name = ?;"
SEARCH_ITEM_BY_CATEGORY = "SELECT * FROM stock WHERE category = ?;"
UPDATE_STOCK = "UPDATE stock WHERE name = ? SET amount = ?;"
VIEW_SOLD_OUT = "SELECT stock.name, manufacturers.delivery_day FROM manufacturers INNER JOIN stock ON amount < 1;"
INSERT_DELIVERY = "INSERT INTO deliveries(delivery_person, phone_number, manufacturer, delivery_day)" \
                  "VALUES (?, ?, ?, ?);"
UPDATE_DELIVERY_PERSON = "UPDATE deliveries SET delivery_person = ?, phone_number = ? WHERE manufacturer = ?;"
SELECT_INVENTORY = "SELECT * FROM stock;"
VIEW_DELIVERY_SCHEDULE = "SELECT * FROM deliveries;"
VIEW_MANUFACTURERS = "SELECT * FROM manufacturers;"



connection = sqlite3.connect("inventory.db")

def create_tables():
    with connection:
        connection.execute(CREATE_STOCK_TABLE)
        connection.execute(CREATE_MANUFACTURER_TABLE)
        connection.execute(CREATE_DELIVERY_TABLE)

def view_inventory():
    cursor = connection.cursor()
    cursor.execute(SELECT_INVENTORY)
    return cursor.fetchall()

def add_item(name, category, cost, amount, manufacturer):
    with connection:
        connection.execute(INSERT_ITEM, (name, category, cost, amount, manufacturer))

def remove_item(name):
    cursor = connection.cursor()
    cursor.execute(REMOVE_ITEM, (name, ))

def search_by_name(name):
    cursor = connection.cursor()
    cursor.execute(SEARCH_ITEM_BY_NAME, (name, ))
    return cursor.fetchone()

def search_by_category(category):
    cursor = connection.cursor()
    cursor.execute(SEARCH_ITEM_BY_CATEGORY, (category, ))
    return cursor.fetchall()

def update_stock(name, amount):
    with connection:
        connection.execute(UPDATE_STOCK, (name, amount))

def check_sold_out():
    cursor = connection.cursor()
    cursor.execute(VIEW_SOLD_OUT)
    return cursor.fetchall()


def view_manufacturers():
    cursor = connection.cursor()
    cursor.execute(VIEW_MANUFACTURERS)
    return cursor.fetchall()

def add_manufacturer(manufacturer, address, delivery_day):
    with connection:
        connection.execute(INSERT_MANUFACTURER, (manufacturer, address, delivery_day))


def create_deliveries(delivery_person, phone_number, manufacturer, delivery_day):
    with connection:
        connection.execute(INSERT_DELIVERY, (delivery_person, phone_number, manufacturer, delivery_day))

def view_deliveries_table():
    cursor = connection.cursor()
    cursor.execute(VIEW_DELIVERY_SCHEDULE)
    return cursor.fetchall()

def update_delivery_person(delivery_person, phone_number, manufacturer):
    with connection:
        connection.execute(UPDATE_DELIVERY_PERSON, (delivery_person, phone_number, manufacturer))



