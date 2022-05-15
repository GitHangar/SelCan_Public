import database


class Admin:
    def __init__(self):
        pass

    def add_user(self, username, email, password):
        database.db.execute("INSERT INTO user(username, email, password) VALUES (?, ?, ?)",
                            (username, email, password))
        database.db.commit()

    def get_user(self, id_user):
        database.imlec.execute("SELECT * FROM user WHERE id = ?", (id_user, ))
        result = database.imlec.fetchone()
        return result

    def rm_user(self, id_user):
        database.db.execute("DELETE FROM user WHERE id = ?", (id_user, ))
        database.db.commit()

    def edit_user(self, id_user, username, name, staff_id, statu_id):
        database.db.execute("UPDATE user SET username = ?, name = ?, staff_id = ?, statu_id = ? WHERE id = ?",
                            (username, name, staff_id, statu_id, id_user))
        database.db.commit()

    def add_statu(self, name):
        database.db.execute("INSERT INTO statu VALUES (NULL,?)", (name, ))
        database.db.commit()

    def get_statu(self, id_statu):
        database.imlec.execute("SELECT * FROM statu WHERE id = ?", (id_statu, ))
        result = database.imlec.fetchone()
        return result

    def rm_statu(self, id_statu):
        database.db.execute("DELETE FROM statu WHERE id = ?", (id_statu, ))
        database.db.commit()

    def edit_statu(self, id_statu, name):
        database.db.execute("UPDATE statu SET name = ? WHERE id = ?", (name, id_statu))
        database.db.commit()