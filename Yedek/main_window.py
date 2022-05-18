import datetime

import database
import product as p
import staff as st
import sign as si
import admin as a
import work

from Window import LoginWindow
from Window import StaffWindow
from Window import ProductWindow
from Window import AdminWindow
from Window import SettingWindow
from Window import MainWindow
from Window import WorkAdd

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time

product = p.Unit()
product_category = p.Category()

staff = st.Staff()
staff_department = st.Department()

sign = si.Sign()
admin = a.Admin()

app = QApplication(sys.argv)

login_window = LoginWindow.Ui_window()
staff_window = StaffWindow.Ui_MainWindow()
product_window = ProductWindow.Ui_MainWindow()
admin_window = AdminWindow.Ui_MainWindow()
setting_window = SettingWindow.Ui_MainWindow()
menu_window = MainWindow.Ui_MainWindow()
work_add_window = WorkAdd.Ui_MainWindow()

main_window = QMainWindow()
form_window = QWidget()
message_window = QMessageBox()

class main:
    def __init__(self):
        self.key = None
        self.boolkey = False

        self.staff_list = []
        self.product_list = []

        login_window.setupUi(main_window)

        login_window.button_login.clicked.connect(self.login_window)
        main_window.show()
        sys.exit(app.exec_())

    def login_window(self):
        username = login_window.line_uname.text()
        password = login_window.line_pass.text()
        is_login = sign.login(username, password)
        if is_login == True:
            is_admin = sign.is_admin(sign.user_info[0])
            if is_admin == True:
                self.admin_window()
            else:
                self.menu_window()
        elif is_login == False:
            message_window.setWindowTitle("Giriş bildirimi")
            message_window.setText("Giriş başarılı değil!")
            message_window.exec()

    def home_window(self):
        pass

    """
    ÜRÜNLER
    """

    def product_window(self):
        product_window.setupUi(main_window)

        self.key = "Product"

        self.get_table()

        product_window.pushButton_add.clicked.connect(self.new_add)
        product_window.pushButton_edit.clicked.connect(self.edit)
        product_window.pushButton_search.clicked.connect(self.search)
        product_window.pushButton_reload.clicked.connect(self.get_table)
        product_window.pushButton_remove.clicked.connect(self.remove)
        product_window.tableWidget.clicked.connect(self.table_select)
        product_window.radioButton_rsure.clicked.connect(self.table_select)

    def new_add(self):
        if self.key == "Product":
            name = product_window.lineEdit_name.text()
            category = product_window.comboBox_category.currentText()
            piece = product_window.spinBox_piece.value()
            product.add_product(name, category, piece)
        elif self.key == "Staff":
            name = staff_window.lineEdit_name.text()
            surname = staff_window.lineEdit_surname.text()
            phone = staff_window.lineEdit_phone.text()
            email = staff_window.lineEdit_email.text()
            salary = staff_window.doubleSpinBox_salary.value()
            department = staff_window.comboBox_department.currentText()
            staff.add_staff(name, surname, phone, email, salary, department)
        elif self.key == "Setting":
            if setting_window.tab_department.isVisible() == True:
                name = setting_window.lineEdit_dname.text()
                staff_department.add(name)
            elif setting_window.tab_category.isVisible() == True:
                name = setting_window.lineEdit_cname.text()
                product_category.add(name)
        elif self.key == "WorkAdd":
            type_product = work_add_window.comboBox_worktype.currentText()
            id_work = work.Task().add(type_product, datetime.datetime.now())
            for id_product, piece_product in self.product_list:
                for id_staff in self.staff_list:
                    work.Product().add(id_work, id_product, piece_product)
                    work.Staff().add(id_work, id_staff)
        self.get_table()
        self.line_clear()

    def remove(self):
        try:
            if self.key == "Product":
                product.rm_product(self.selected_remove[0].text())
                product_window.tableWidget.clear()
                self.get_table()
            elif self.key == "Staff":
                staff.rm_staff(self.selected_remove[0].text())
                staff_window.tableWidget.clear()
                self.get_table()
            elif self.key == "Setting":
                if setting_window.tab_category.isVisible() == True:
                    product_category.rm(self.selected_remove[0].text())
                elif setting_window.tab_department.isVisible() == True:
                    staff_department.rm(self.selected_remove[0].text())
                setting_window.tableWidget_home.clear()
                setting_window.tableWidget_backup.clear()
                self.get_table()

        except TypeError:
            pass
        except RuntimeError:
            pass


    def edit(self):
        try:
            if self.key == "Product":
                id_product = product_window.tableWidget.selectedItems()[0].text()
                name = product_window.lineEdit_ename.text()
                category = product_window.comboBox_ecategory.currentText()
                piece = product_window.spinBox_epiece.value()
                product.edit_product(id_product, name, category, piece)
            elif self.key == "Staff":
                id_staff = staff_window.tableWidget.selectedItems()[0].text()
                name = staff_window.lineEdit_ename.text()
                surname = staff_window.lineEdit_esurname.text()
                phone = staff_window.lineEdit_ephone.text()
                mail = staff_window.lineEdit_eemail.text()
                salary = staff_window.doubleSpinBox_esalary.value()
                department = staff_window.comboBox_edepartment.currentText()
                staff.edit_staff(id_staff, name, surname, phone, mail, salary, department)
            elif self.key == "Setting":
                if setting_window.tab_category.isVisible() == True:
                    id_category = setting_window.lineEdit_cid.text()
                    name = setting_window.lineEdit_cname.text()
                    product_category.edit(id_category, name)
                elif setting_window.tab_department.isVisible() == True:
                    id_department = setting_window.lineEdit_did.text()
                    name = setting_window.lineEdit_dname.text()
                    staff_department.edit(id_department, name)
            self.get_table()
        except IndexError:
            message_window.setWindowTitle("Hata!")
            message_window.setText("Tablodan bir veri seçiniz")
            message_window.exec()


    def search(self):
        if self.key == "Product":
            product_window.tableWidget.clear()
            product_window.tableWidget.setHorizontalHeaderLabels(('ID', 'Name', 'Category', 'Piece'))
            product_window.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            search = product_window.lineEdit_searchval.text()
            result = product.query_product(search)
            if bool(result) == True:
                for row_index, row_data in enumerate(result):
                    for column_index, column_data in enumerate(row_data):
                        product_window.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
                        self.line_clear()
        elif self.key == "Staff":
            staff_window.tableWidget.clear()
            staff_window.tableWidget.setHorizontalHeaderLabels((
                "ID", "Name", "Surname", "Phone", "Email", "Salary", "Department"))
            staff_window.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            search = staff_window.lineEdit_searchval.text()
            result = staff.query_staff(search)
            if bool(result):
                for row_index, row_data in enumerate(result):
                    for column_index, column_data in enumerate(row_data):
                        staff_window.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
                        self.line_clear()
        else:
            pass

    def table_select(self):
        try:
            self.line_clear()
            if self.key == "Product":
                selected_staff = product_window.tableWidget.selectedItems()

                product_window.lineEdit_rid.setText(selected_staff[0].text())
                product_window.lineEdit_rname.setText(selected_staff[1].text())
                product_window.lineEdit_rcategory.setText(selected_staff[2].text())
                product_window.lineEdit_rpiece.setText(selected_staff[3].text())

                product_window.lineEdit_ename.setText(selected_staff[1].text())
                product_window.comboBox_ecategory.setCurrentText(selected_staff[2].text())
                product_window.spinBox_epiece.setValue(int(selected_staff[3].text()))
                if product_window.radioButton_rsure.isChecked() == True:
                    self.selected_remove = selected_staff
                    product_window.pushButton_remove.setEnabled(True)
                else:
                    product_window.pushButton_remove.setEnabled(False)

            elif self.key == "Staff":
                selected_staff = staff_window.tableWidget.selectedItems()

                staff_window.lineEdit_rid.setText(selected_staff[0].text())
                staff_window.lineEdit_rname.setText(selected_staff[1].text())
                staff_window.lineEdit_rmail.setText(selected_staff[2].text())
                staff_window.lineEdit_rphone.setText(selected_staff[3].text())
                staff_window.lineEdit_rsalary.setText(selected_staff[4].text())
                staff_window.lineEdit_rdepartment.setText(selected_staff[5].text())

                staff_window.lineEdit_ename.setText(selected_staff[1].text())
                staff_window.lineEdit_esurname.setText(selected_staff[2].text())
                staff_window.lineEdit_ephone.setText(selected_staff[3].text())
                staff_window.lineEdit_eemail.setText(selected_staff[4].text())
                staff_window.doubleSpinBox_esalary.setValue(float(selected_staff[5].text()))
                staff_window.comboBox_edepartment.setCurrentText(selected_staff[6].text())
                if staff_window.radioButton_rsure.isChecked() == True:
                    staff_window.pushButton_remove.setEnabled(True)
                else:
                    staff_window.pushButton_remove.setEnabled(False)

            elif self.key == "Staff":
                selected_staff = staff_window.tableWidget.selectedItems()

                staff_window.lineEdit_rid.setText(selected_staff[0].text())
                staff_window.lineEdit_rname.setText(f"{selected_staff[1].text()} {selected_staff[2].text()}")
                staff_window.lineEdit_rphone.setText(selected_staff[3].text())
                staff_window.lineEdit_rmail.setText(selected_staff[4].text())
                staff_window.lineEdit_rsalary.setText(selected_staff[5].text())
                staff_window.lineEdit_rdepartment.setText(selected_staff[6].text())
                if staff_window.radioButton_rsure.isChecked() == True:
                    staff_window.pushButton_remove.setEnabled(True)
                else:
                    staff_window.pushButton_remove.setEnabled(False)

            elif self.key == "Setting":
                if setting_window.tab_category.isVisible() == True:
                    selected_staff = setting_window.tableWidget_home.selectedItems()

                    setting_window.lineEdit_cid.setText(selected_staff[0].text())
                    setting_window.lineEdit_cname.setText(selected_staff[1].text())

                    result = staff.department_query(selected_staff[0].text())
                else:
                    selected_staff = setting_window.tableWidget_home.selectedItems()
                    setting_window.lineEdit_did.setText(selected_staff[0].text())
                    setting_window.lineEdit_dname.setText(selected_staff[1].text())
                    result = staff.department_query(selected_staff[0].text())

                setting_window.tableWidget_backup.setRowCount(100)
                setting_window.tableWidget_backup.setColumnCount(7)
                setting_window.tableWidget_backup.clear()
                setting_window.tableWidget_backup.setHorizontalHeaderLabels((
                        "ID", "Name", "Surname", "Phone", "Email", "Salary", "Department"))
                setting_window.tableWidget_backup.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                for row_index, row_data in enumerate(result):
                    for column_index, column_data in enumerate(row_data):
                        setting_window.tableWidget_backup.setItem(row_index, column_index,
                                                                  QTableWidgetItem(str(column_data)))
            elif self.key == "WorkAdd":
                if len(work_add_window.tableWidget_staff.selectedRanges()) == 1:
                    selected_staff = work_add_window.tableWidget_staff.selectedItems()

                    work_add_window.lineEdit_staffid.setText(selected_staff[0].text())
                    work_add_window.lineEdit_staffname.setText(selected_staff[1].text())
                    work_add_window.lineEdit_staffmail.setText(selected_staff[2].text())

                    work_add_window.lineEdit_productid.clear()
                    work_add_window.lineEdit_productname.clear()
                    work_add_window.spinBox_productpiece.clear()

                elif len(work_add_window.tableWidget_product.selectedRanges()) == 1:
                    selected_product = work_add_window.tableWidget_product.selectedItems()

                    work_add_window.lineEdit_productid.setText(selected_product[0].text())
                    work_add_window.lineEdit_productname.setText(selected_product[1].text())

                    work_add_window.lineEdit_staffid.clear()
                    work_add_window.lineEdit_staffname.clear()
                    work_add_window.lineEdit_staffmail.clear()
                work_add_window.tableWidget_staff.clearSelection()
                work_add_window.tableWidget_product.clearSelection()

        except IndexError:
            pass
        except AttributeError:
            pass

    def get_table(self):
        if self.key == "Product":
            product_window.tableWidget.clear()
            product_window.tableWidget.setHorizontalHeaderLabels(('ID', 'Name', 'Category', 'Piece'))
            product_window.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            result = product.all_product()
            for row_index, row_data in enumerate(result):
                for column_index, column_data in enumerate(row_data):
                    product_window.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
            self.line_clear()
            product_window.lineEdit_all.setText(str(product.all_piece()))

        elif self.key == "Staff":
            staff_window.tableWidget.clear()
            staff_window.tableWidget.setHorizontalHeaderLabels((
                    "ID", "Name", "Surname", "Phone", "Email", "Salary", "Department"))
            staff_window.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            result = staff.all_staff()
            for row_index, row_data in enumerate(result):
                for column_index, column_data in enumerate(row_data):
                    staff_window.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
            self.line_clear()
            staff_window.lineEdit_all.setText(str(staff.total_staff()))
            staff_window.lineEdit_allval.setText(str(staff.total_salary()))

        elif self.key == "Setting":
            setting_window.tableWidget_home.clear()
            setting_window.tableWidget_backup.clear()
            setting_window.tableWidget_home.setHorizontalHeaderLabels((
                        "ID", "Name"))
            setting_window.tableWidget_home.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            if setting_window.tab_category.isVisible() == True:
                print("Category")
                result = product_category.all_query()
            else:
                print("Department")
                result = staff_department.all_query()
            for row_index, row_data in enumerate(result):
                for column_index, column_data in enumerate(row_data):
                    setting_window.tableWidget_home.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
            self.line_clear()

        elif self.key == "WorkAdd":
            work_add_window.tableWidget_staff.clear()
            work_add_window.tableWidget_product.clear()

            work_add_window.tableWidget_staff.setHorizontalHeaderLabels(("ID", "Name", "Email"))
            work_add_window.tableWidget_product.setHorizontalHeaderLabels(("ID", "Name", "Piece"))

            work_add_window.tableWidget_staff.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            work_add_window.tableWidget_product.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            result = staff.get_workstaff()
            work_add_window.tableWidget_staff.setRowCount(len(result))
            for row_index, row_data in enumerate(result):
                for column_index, column_data in enumerate(row_data):
                    work_add_window.tableWidget_staff.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
            database.imlec.execute("SELECT id, name, piece FROM product")
            result = database.imlec.fetchall()
            work_add_window.tableWidget_product.setRowCount(len(result))
            for row_index, row_data in enumerate(result):
                for column_index, column_data in enumerate(row_data):
                    work_add_window.tableWidget_product.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))
            self.line_clear()

    def line_clear(self):
        if self.key == "Product":
            product_window.lineEdit_name.clear()
            product_window.spinBox_piece.clear()
            product_window.comboBox_category.setCurrentIndex(-1)

            product_window.lineEdit_rname.clear()
            product_window.lineEdit_rid.clear()
            product_window.lineEdit_rpiece.clear()
            product_window.lineEdit_rcategory.clear()

            product_window.lineEdit_ename.clear()
            product_window.comboBox_ecategory.setCurrentIndex(-1)
            product_window.spinBox_epiece.clear()

        elif self.key == "Staff":
            staff_window.lineEdit_name.clear()
            staff_window.lineEdit_surname.clear()
            staff_window.lineEdit_phone.clear()
            staff_window.lineEdit_email.clear()
            staff_window.doubleSpinBox_salary.clear()
            staff_window.comboBox_department.setCurrentIndex(-1)

            staff_window.lineEdit_rid.clear()
            staff_window.lineEdit_rname.clear()
            staff_window.lineEdit_rphone.clear()
            staff_window.lineEdit_rmail.clear()
            staff_window.lineEdit_rdepartment.clear()
            staff_window.lineEdit_rsalary.clear()

            staff_window.lineEdit_ename.clear()
            staff_window.lineEdit_eemail.clear()
            staff_window.lineEdit_ephone.clear()
            staff_window.lineEdit_esurname.clear()
            staff_window.doubleSpinBox_esalary.clear()
            staff_window.comboBox_edepartment.setCurrentIndex(-1)

        elif self.key == "Setting":
            setting_window.lineEdit_cname.clear()
            setting_window.lineEdit_cid.clear()
            setting_window.lineEdit_did.clear()
            setting_window.lineEdit_dname.clear()

        elif self.key == "WorkAdd":
            work_add_window.lineEdit_staffid.clear()
            work_add_window.lineEdit_staffname.clear()
            work_add_window.lineEdit_staffmail.clear()

            work_add_window.lineEdit_productid.clear()
            work_add_window.lineEdit_productname.clear()
            work_add_window.spinBox_productpiece.clear()

            work_add_window.listWidget_staff.clear()
            work_add_window.listWidget_product.clear()
            self.staff_list.clear()
            self.product_list.clear()


    """
    ADMİN
    """

    def admin_window(self):
        self.key = "Admin"
        admin_window.setupUi(main_window)

        admin_window.pushButton_products.clicked.connect(self.product_window)
        admin_window.pushButton_staff.clicked.connect(self.staff_window)
        admin_window.pushButton_company.clicked.connect(self.setting_window)
        admin_window.pushButton_logout.clicked.connect(exit)

    """
    STAFF
    """

    def staff_window(self):
        self.key = "Staff"
        staff_window.setupUi(main_window)

        self.get_table()

        staff_window.pushButton_add.clicked.connect(self.new_add)
        staff_window.pushButton_remove.clicked.connect(self.remove)
        staff_window.pushButton_search.clicked.connect(self.search)
        staff_window.pushButton_reload.clicked.connect(self.get_table)
        staff_window.pushButton_edit.clicked.connect(self.edit)

        staff_window.radioButton_rsure.clicked.connect(self.table_select)
        staff_window.tableWidget.clicked.connect(self.table_select)

    def setting_window(self):
        self.key = "Setting"

        setting_window.setupUi(main_window)
        self.get_table()

        setting_window.pushButton_add.clicked.connect(self.new_add)
        setting_window.pushButton_rm.clicked.connect(self.remove)
        setting_window.pushButton_upd.clicked.connect(self.edit)
        setting_window.pushButton_reload.clicked.connect(self.get_table)
        setting_window.tabWidget.currentChanged.connect(self.get_table)
        setting_window.tableWidget_home.clicked.connect(self.table_select)

    def menu_window(self):
        menu_window.setupUi(main_window)

        menu_window.pushButton_workstart.clicked.connect(self.workadd_window)
        menu_window.pushButton_products.clicked.connect(self.product_window)

    def workadd_window(self):
        self.key = "WorkAdd"

        work_add_window.setupUi(main_window)
        self.get_table()

        work_add_window.tableWidget_staff.clicked.connect(self.table_select)
        work_add_window.tableWidget_product.clicked.connect(self.table_select)
        work_add_window.comboBox_worktype.currentText()

        work_add_window.pushButton_add.clicked.connect(self.list_add)
        work_add_window.pushButton_confirm.clicked.connect(self.new_add)

    def list_add(self):
        if work_add_window.lineEdit_staffid.text() != "":
            self.staff_list.append(work_add_window.lineEdit_staffid.text())

            work_add_window.listWidget_staff.addItem(
                f"{work_add_window.lineEdit_staffid.text()},\
    {work_add_window.lineEdit_staffname.text()},\
    {work_add_window.lineEdit_staffmail.text()}")
        elif work_add_window.lineEdit_productid.text() != "":

            self.product_list.append(
                (work_add_window.lineEdit_productid.text(), work_add_window.spinBox_productpiece.text()))

            work_add_window.listWidget_product.addItem(
                f"{work_add_window.lineEdit_productid.text()},\
    {work_add_window.lineEdit_productname.text()},\
    {work_add_window.spinBox_productpiece.text()}")