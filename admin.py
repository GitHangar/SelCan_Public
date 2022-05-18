import database
import sqlite3


class Admin:
    def __init__(self):
        pass

    @staticmethod
    def add_user(self, username, email, password):
        database.db.execute("INSERT INTO user(username, email, password) VALUES (?, ?, ?)",
                            (username, email, password))
        database.db.commit()

    @staticmethod
    def get_user(self, id_user):
        database.imlec.execute("SELECT * FROM user WHERE id = ?", (id_user, ))
        result = database.imlec.fetchone()
        return result

    @staticmethod
    def rm_user(id_user):
        try:
            database.db.execute("DELETE FROM user WHERE id = ?", (id_user, ))
            database.db.commit()
        except sqlite3.IntegrityError:
            pass

    @staticmethod
    def edit_user(self, id_user, username, email, statu_id, staff_id = None):
        database.db.execute("UPDATE user SET username = ?, email = ?, staff_id = ?, statu_id = ? WHERE id = ?",
                            (username, email, staff_id, statu_id, id_user))
        database.db.commit()

    @staticmethod
    def add_statu(self, name):
        database.db.execute("INSERT INTO statu VALUES (NULL,?)", (name, ))
        database.db.commit()

    @staticmethod
    def get_statu(self, id_statu):
        database.imlec.execute("SELECT * FROM statu WHERE id = ?", (id_statu, ))
        result = database.imlec.fetchone()
        return result

    @staticmethod
    def rm_statu(self, id_statu):
        try:
            database.db.execute("DELETE FROM statu WHERE id = ?", (id_statu, ))
            database.db.commit()
        except sqlite3.IntegrityError:
            pass

    @staticmethod
    def edit_statu(self, id_statu, name):
        database.db.execute("UPDATE statu SET name = ? WHERE id = ?", (name, id_statu))
        database.db.commit()
