import database


class Sign:
    def __init__(self):
        self.user_info = set()

    def login(self, username, password):
        database.imlec.execute("SELECT id, username, email, password FROM user\
        WHERE (username = ? OR email = ?) AND password = ?", (username, username, password))
        result = database.imlec.fetchone()
        self.user_info = result
        return bool(result)

    def fargot_pass(self, email):
        database.imlec.execute("SELECT email FROM user WHERE email = ?", (email, ))
        if email == database.imlec.fetchone()[0]:
            pass
        else:
            pass

    def is_admin(self, id_user):
        try:
            database.imlec.execute("SELECT statu.name FROM user, statu WHERE user.id = ? and user.statu_id = statu.id", (id_user, ))
            result = database.imlec.fetchone()[0]
            if result == "Admin":
                return bool(result)
            else:
                print(bool(result))
                return bool(result)
        except TypeError:
            pass