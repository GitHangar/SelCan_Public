import database


class Task:
    def __init__(self):
        pass

    def add(self, type, datetime):
        database.db.execute("INSERT INTO work(type, created_date) VALUES (?, ?)",
                            (type, datetime))
        database.db.commit()
        result = self.all_query()
        return result[-1][0]

    @staticmethod
    def rm(id_work):
        database.db.execute("DELETE FROM work WHERE id = ?", (id_work, ))
        database.db.commit()

    @staticmethod
    def get(work_id):
        database.imlec.execute(
            "SELECT work.id, \
            work.type, \
            staff.name, \
            staff.surname, \
            staff.email, \
            product.name, \
            product.category, \
            work_product.product_piece \
            FROM work, \
            work_staff, \
            staff, product, \
            work_product \
            WHERE work.id = ? \
            AND work_staff.staff_id = staff.id \
            AND work_product.product_id = product.id",
            (work_id, )
        )
        result = database.imlec.fetchall()
        return result

    @staticmethod
    def all_query():
        database.imlec.execute("SELECT * FROM work")
        result = database.imlec.fetchall()
        return result


class Product:
    def __init__(self):
        pass

    def add(self, work_id, product_id, product_piece):
        database.db.execute("INSERT INTO work_product(work_id, product_id, product_piece) VALUES(?, ?, ?)",
                            (work_id, product_id, product_piece))
        database.db.commit()


class Staff:
    def __init__(self):
        pass

    def add(self, work_id, staff_id):
        database.db.execute("INSERT INTO work_staff(work_id, staff_id) VALUES (?, ?)",
                            (work_id, staff_id))
        database.db.commit()
