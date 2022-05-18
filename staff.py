import database
import sqlite3


class Staff:
    def __init__(self):
        pass

    @staticmethod
    def add_staff(name, surname, phone, email, salary, department_id):
        database.db.execute("INSERT INTO staff(name, surname, phone, email, salary, department_id) VALUES \
        (?, ?, ?, ?, ?, ?)", (name, surname, phone, email, salary, department_id))
        database.db.commit()

    @staticmethod
    def rm_staff(id_staff):
        database.db.execute("DELETE FROM staff WHERE id = ?", (id_staff, ))
        database.db.commit()

    @staticmethod
    def all_staff():
        database.imlec.execute("SELECT * FROM staff")
        result = database.imlec.fetchall()
        return result

    @staticmethod
    def get_staff(id_staff):
        database.imlec.execute("SELECT * FROM staff WHERE id = ?", (id_staff, ))
        result = database.imlec.fetchone()
        return result

    @staticmethod
    def query_staff(value):
        database.imlec.execute("SELECT * FROM staff WHERE id = ? OR name = ? OR salary = ?",
                               (value, value, value))
        result = database.imlec.fetchall()
        return result

    @staticmethod
    def get_workstaff():
        database.imlec.execute("SELECT id, name, surname, email FROM staff")
        result = database.imlec.fetchall()
        new_result = []
        for staff_id, name, surname, email in result:
            full_name = f"{name} {surname}"
            new_result.append((staff_id, full_name, email))
        return new_result

    @staticmethod
    def department_query(id_department):
        database.imlec.execute("SELECT * FROM staff WHERE department_id = ?",
                               (id_department, ))
        result = database.imlec.fetchall()
        return result

    @staticmethod
    def edit_staff(id_staff, name, surname, phone, email, salary, department):
        database.db.execute(
            "UPDATE staff SET\
             name = ?, \
             surname = ?, \
             phone = ?, \
             email = ?, \
             salary = ?, \
             department = ? \
             WHERE id = ?",
            (name, surname, phone, email, salary, department, id_staff)
        )
        database.db.commit()

    def total_staff(self):
        result = self.all_staff()
        amount = 0
        for value in result:
            amount += 1
        return amount

    def total_salary(self):
        result = self.all_staff()
        amount = 0
        for i in result:
            amount += i[5]
        return amount

class Department:
    @staticmethod
    def add(name):
        try:
            database.db.execute("INSERT INTO department(name) VALUES (?)",
                                (name, ))
            database.db.commit()
        except sqlite3.IntegrityError:
            pass

    @staticmethod
    def edit(department_id, name):
        database.db.execute("UPDATE department SET name = ? WHERE id = ?",
                            (name, department_id))
        database.db.commit()

    @staticmethod
    def all_query():
        database.imlec.execute("SELECT * FROM department")
        result = database.imlec.fetchall()
        return result

    @staticmethod
    def rm(department_id):
        database.db.execute("DELETE FROM department WHERE id = ?",
                            (department_id, ))
        database.db.commit()
