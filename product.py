import database


class Unit:
    def __init__(self):
        pass

    def add_product(self, name, category, piece):
        database.db.execute("INSERT INTO Product VALUES (NULL, ?, ?, ?)",
                            (name, category, piece))
        database.db.commit()

    def rm_product(self, id_product):
        database.db.execute(f"DELETE FROM Product WHERE id = ?",
                            (id_product, ))
        database.db.commit()

    def all_product(self):
        database.imlec.execute("SELECT * FROM product")
        result = database.imlec.fetchall()
        return result

    def get_product(self, id_product):
        database.imlec.execute("SELECT * FROM product WHERE product_id = ?",
                               (id_product, ))
        result = database.imlec.fetchone()
        return result

    def query_product(self, value):
        database.imlec.execute("SELECT * FROM product WHERE id = ? OR name = ? OR  category = ?", (value, value, value))
        result = database.imlec.fetchall()
        return result

    def edit_product(self, id_product, name, category, piece):
        database.db.execute("UPDATE product SET name = ?, category = ?, piece = ? WHERE id = ? ",
                            (name, category, piece, id_product))
        database.db.commit()

    def all_piece(self):
        result = self.all_product()
        unit_piece = 0
        for i in result:
            unit_piece += i[3]
        return unit_piece

class Category:
    def add(self, name):
        database.db.execute("INSERT INTO Category(Name) VALUES (?)", (name, ))
        database.db.commit()
        print("Add")

    def rm(self, id):
        database.db.execute("DELETE FROM Category WHERE id = ?", (id, ))
        database.db.commit()

    def all_query(self):
        database.imlec.execute("SELECT * FROM Category")
        result = database.imlec.fetchall()
        return result
