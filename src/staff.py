from . import database
import sqlite3


class Staff:
    def __init__(self):
        pass

    def add_staff(self, name, surname, phone, email, salary, department):
        database.db.execute("INSERT INTO staff(name, surname, phone, email, salary, department) VALUES \
        (?, ?, ?, ?, ?, ?)", (name, surname, phone, email, salary, department))
        database.db.commit()

    def rm_staff(self, id_staff):
        database.db.execute("DELETE FROM staff WHERE id = ?", (id_staff, ))
        database.db.commit()

    def all_staff(self):
        database.imlec.execute("SELECT * FROM staff")
        result = database.imlec.fetchall()
        return result

    def get_staff(self, id_staff):
        database.imlec.execute("SELECT * FROM staff WHERE id = ?", (id_staff, ))
        result = database.imlec.fetchone()
        return result

    def query_staff(self, value):
        database.imlec.execute("SELECT * FROM staff WHERE id = ? OR name = ? OR salary = ?", (value, value, value))
        result = database.imlec.fetchall()
        return result

    def department_query(self, id_department):
        database.imlec.execute("SELECT * FROM staff WHERE department_id = ?", (id_department, ))
        result = database.imlec.fetchall()
        return result

    def edit_staff(self, id_staff, name, surname, phone, email, salary, department):
        database.db.execute("UPDATE staff SET name = ?, surname = ?, phone = ?, email = ?, salary = ?, department = ? \
        WHERE id = ?", (name, surname, phone, email, salary, department, id_staff))
        database.db.commit()

    def total_staff(self):
        result = self.all_staff()
        amount = 0
        for i in result:
            amount += 1
        return amount

    def total_salary(self):
        result = self.all_staff()
        amount = 0
        for i in result:
            amount += i[5]
        return amount

class Department:
    def add(self, name):
        try:
            database.db.execute("INSERT INTO department(name) VALUES (?)", (name, ))
            database.db.commit()
        except sqlite3.IntegrityError:
            pass

    def edit(self, department_id, name):
        database.db.execute("UPDATE department SET name = ? WHERE id = ?", (name, department_id))
        database.db.commit()

    def all_query(self):
        database.imlec.execute("SELECT * FROM department")
        result = database.imlec.fetchall()
        return result

    def rm(self, id):
        database.db.execute("DELETE FROM department WHERE id = ?", (id, ))
        database.db.commit()
