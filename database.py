import sqlite3

db = sqlite3.connect("database.db")
db.execute("PRAGMA foreign_keys = 1")
imlec = db.cursor()

def create():
    db.execute("CREATE TABLE IF NOT EXISTS Staff (\
    id INTEGER PRIMARY KEY AUTOINCREMENT,\
     name varchar,\
      surname varchar,\
       phone INTEGER,\
       email varchar,\
       salary INTEGER,\
       department_id INTEGER,\
       FOREIGN KEY(department_id) REFERENCES department(id))")

    db.execute("CREATE TABLE IF NOT EXISTS Product (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
         name varchar,\
          category varchar,\
           piece INTEGER)"
    )

    db.execute("CREATE TABLE IF NOT EXISTS SolidProduct (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
         price INTEGER,\
          key INTEGER,\
           staff_id INTEGER,\
            provider_id INTEGER,\
        FOREIGN KEY(provider_id) REFERENCES Provider(id),\
        FOREIGN KEY(staff_id) REFERENCES Staff(id))"
    )

    db.execute("CREATE TABLE IF NOT EXISTS BuyProduct (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
         price INTEGER,\
          product_id INTEGER,\
           staff_id INTEGER,\
            provider_id INTEGER,\
        FOREIGN KEY(product_id) REFERENCES Product(id),\
        FOREIGN KEY(staff_id) REFERENCES Staff(id)\
        FOREIGN KEY(provider_id) REFERENCES Provider(id))"
    )

    db.execute("CREATE TABLE IF NOT EXISTS Provider (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
         name varchar,\
          phone INTEGER,\
           mail varchar)"
    )

    db.execute("CREATE TABLE IF NOT EXISTS User(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        username varchar,\
        email varchar,\
        password text,\
        staff_id INTEGER,\
        statu_id INTEGER,\
        FOREIGN KEY(staff_id) REFERENCES Staff(id) ON DELETE CASCADE,\
        FOREIGN KEY(statu_id) REFERENCES Statu(id) ON DELETE CASCADE)"
    )

    db.execute("CREATE TABLE IF NOT EXISTS Statu (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
         name varchar)"
    )

    db.execute("CREATE TABLE IF NOT EXISTS Department (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
         name varchar NOT NULL,\
         CHECK(name <> ''))"
    )

    db.execute("CREATE TABLE IF NOT EXISTS Category (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
         name varchar NOT NULL)"
    )

    db.execute("CREATE TABLE IF NOT EXISTS UsedProduct (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
         product_id INTEGER,\
          staff_id INTEGER,\
        FOREIGN KEY(product_id) REFERENCES Product(id),\
        FOREIGN KEY(staff_id) REFERENCES Staff(id))"
    )

    db.commit()