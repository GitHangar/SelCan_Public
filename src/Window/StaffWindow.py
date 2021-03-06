# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StaffWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1209, 720))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_searchval = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_searchval.setMaximumSize(QtCore.QSize(525, 16777215))
        self.lineEdit_searchval.setObjectName("lineEdit_searchval")
        self.gridLayout.addWidget(self.lineEdit_searchval, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 2, 1, 2)
        self.comboBox_searchtype = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_searchtype.setEnabled(False)
        self.comboBox_searchtype.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_searchtype.setToolTipDuration(-1)
        self.comboBox_searchtype.setMaxVisibleItems(5)
        self.comboBox_searchtype.setObjectName("comboBox_searchtype")
        self.comboBox_searchtype.addItem("")
        self.comboBox_searchtype.addItem("")
        self.comboBox_searchtype.addItem("")
        self.gridLayout.addWidget(self.comboBox_searchtype, 3, 2, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 3, 3, 1, 1)
        self.pushButton_reload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reload.setObjectName("pushButton_reload")
        self.gridLayout.addWidget(self.pushButton_reload, 1, 2, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(525, 16777215))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_add = QtWidgets.QWidget()
        self.tab_add.setObjectName("tab_add")
        self.layoutWidget = QtWidgets.QWidget(self.tab_add)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 461, 245))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_add = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout_2.addWidget(self.pushButton_add, 7, 0, 1, 3)
        self.comboBox_salarytype = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_salarytype.setEnabled(False)
        self.comboBox_salarytype.setObjectName("comboBox_salarytype")
        self.comboBox_salarytype.addItem("")
        self.comboBox_salarytype.addItem("")
        self.comboBox_salarytype.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_salarytype, 4, 2, 1, 1)
        self.label_salary = QtWidgets.QLabel(self.layoutWidget)
        self.label_salary.setObjectName("label_salary")
        self.gridLayout_2.addWidget(self.label_salary, 4, 0, 1, 1)
        self.lineEdit_surname = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_surname.setText("")
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.gridLayout_2.addWidget(self.lineEdit_surname, 1, 1, 1, 2)
        self.label_name = QtWidgets.QLabel(self.layoutWidget)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 1)
        self.label_company = QtWidgets.QLabel(self.layoutWidget)
        self.label_company.setEnabled(False)
        self.label_company.setObjectName("label_company")
        self.gridLayout_2.addWidget(self.label_company, 6, 0, 1, 1)
        self.label_department = QtWidgets.QLabel(self.layoutWidget)
        self.label_department.setObjectName("label_department")
        self.gridLayout_2.addWidget(self.label_department, 5, 0, 1, 1)
        self.comboBox_company = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_company.setEnabled(False)
        self.comboBox_company.setEditable(False)
        self.comboBox_company.setDuplicatesEnabled(False)
        self.comboBox_company.setObjectName("comboBox_company")
        self.gridLayout_2.addWidget(self.comboBox_company, 6, 1, 1, 2)
        self.comboBox_department = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_department.setObjectName("comboBox_department")
        self.comboBox_department.addItem("")
        self.comboBox_department.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_department, 5, 1, 1, 2)
        self.lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout_2.addWidget(self.lineEdit_name, 0, 1, 1, 2)
        self.doubleSpinBox_salary = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_salary.setEnabled(True)
        self.doubleSpinBox_salary.setMinimumSize(QtCore.QSize(156, 26))
        self.doubleSpinBox_salary.setSizeIncrement(QtCore.QSize(0, 0))
        self.doubleSpinBox_salary.setMouseTracking(True)
        self.doubleSpinBox_salary.setTabletTracking(True)
        self.doubleSpinBox_salary.setWhatsThis("")
        self.doubleSpinBox_salary.setAccessibleName("")
        self.doubleSpinBox_salary.setSpecialValueText("")
        self.doubleSpinBox_salary.setProperty("showGroupSeparator", False)
        self.doubleSpinBox_salary.setPrefix("")
        self.doubleSpinBox_salary.setSuffix("")
        self.doubleSpinBox_salary.setMaximum(9999999999.0)
        self.doubleSpinBox_salary.setObjectName("doubleSpinBox_salary")
        self.gridLayout_2.addWidget(self.doubleSpinBox_salary, 4, 1, 1, 1)
        self.label_surname = QtWidgets.QLabel(self.layoutWidget)
        self.label_surname.setObjectName("label_surname")
        self.gridLayout_2.addWidget(self.label_surname, 1, 0, 1, 1)
        self.label_mail = QtWidgets.QLabel(self.layoutWidget)
        self.label_mail.setObjectName("label_mail")
        self.gridLayout_2.addWidget(self.label_mail, 3, 0, 1, 1)
        self.lineEdit_email = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout_2.addWidget(self.lineEdit_email, 3, 1, 1, 2)
        self.label_phone = QtWidgets.QLabel(self.layoutWidget)
        self.label_phone.setObjectName("label_phone")
        self.gridLayout_2.addWidget(self.label_phone, 2, 0, 1, 1)
        self.lineEdit_phone = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.gridLayout_2.addWidget(self.lineEdit_phone, 2, 1, 1, 2)
        self.tabWidget.addTab(self.tab_add, "")
        self.tab_remove = QtWidgets.QWidget()
        self.tab_remove.setObjectName("tab_remove")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_remove)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 481, 213))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_rmail = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_rmail.setReadOnly(True)
        self.lineEdit_rmail.setObjectName("lineEdit_rmail")
        self.gridLayout_3.addWidget(self.lineEdit_rmail, 3, 1, 1, 1)
        self.lineEdit_rsalary = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_rsalary.setReadOnly(True)
        self.lineEdit_rsalary.setObjectName("lineEdit_rsalary")
        self.gridLayout_3.addWidget(self.lineEdit_rsalary, 4, 1, 1, 1)
        self.label_rname = QtWidgets.QLabel(self.layoutWidget1)
        self.label_rname.setObjectName("label_rname")
        self.gridLayout_3.addWidget(self.label_rname, 1, 0, 1, 1)
        self.radioButton_rsure = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_rsure.setObjectName("radioButton_rsure")
        self.gridLayout_3.addWidget(self.radioButton_rsure, 6, 0, 1, 1)
        self.lineEdit_rphone = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_rphone.setReadOnly(True)
        self.lineEdit_rphone.setObjectName("lineEdit_rphone")
        self.gridLayout_3.addWidget(self.lineEdit_rphone, 2, 1, 1, 1)
        self.pushButton_remove = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_remove.setEnabled(False)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.gridLayout_3.addWidget(self.pushButton_remove, 6, 1, 1, 1)
        self.lineEdit_rid = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_rid.setAcceptDrops(True)
        self.lineEdit_rid.setReadOnly(True)
        self.lineEdit_rid.setObjectName("lineEdit_rid")
        self.gridLayout_3.addWidget(self.lineEdit_rid, 0, 1, 1, 1)
        self.label_rmail = QtWidgets.QLabel(self.layoutWidget1)
        self.label_rmail.setObjectName("label_rmail")
        self.gridLayout_3.addWidget(self.label_rmail, 3, 0, 1, 1)
        self.lineEdit_rname = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_rname.setReadOnly(True)
        self.lineEdit_rname.setObjectName("lineEdit_rname")
        self.gridLayout_3.addWidget(self.lineEdit_rname, 1, 1, 1, 1)
        self.label_rsalary = QtWidgets.QLabel(self.layoutWidget1)
        self.label_rsalary.setObjectName("label_rsalary")
        self.gridLayout_3.addWidget(self.label_rsalary, 4, 0, 1, 1)
        self.label_rid = QtWidgets.QLabel(self.layoutWidget1)
        self.label_rid.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_rid.setObjectName("label_rid")
        self.gridLayout_3.addWidget(self.label_rid, 0, 0, 1, 1)
        self.label_rphone = QtWidgets.QLabel(self.layoutWidget1)
        self.label_rphone.setObjectName("label_rphone")
        self.gridLayout_3.addWidget(self.label_rphone, 2, 0, 1, 1)
        self.label_rdepartment = QtWidgets.QLabel(self.layoutWidget1)
        self.label_rdepartment.setObjectName("label_rdepartment")
        self.gridLayout_3.addWidget(self.label_rdepartment, 5, 0, 1, 1)
        self.lineEdit_rdepartment = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_rdepartment.setObjectName("lineEdit_rdepartment")
        self.gridLayout_3.addWidget(self.lineEdit_rdepartment, 5, 1, 1, 1)
        self.tabWidget.addTab(self.tab_remove, "")
        self.tab_edit = QtWidgets.QWidget()
        self.tab_edit.setAccessibleName("")
        self.tab_edit.setObjectName("tab_edit")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_edit)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 30, 461, 245))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_edit = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.gridLayout_4.addWidget(self.pushButton_edit, 7, 0, 1, 3)
        self.comboBox_esalarytype = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_esalarytype.setEnabled(False)
        self.comboBox_esalarytype.setObjectName("comboBox_esalarytype")
        self.comboBox_esalarytype.addItem("")
        self.comboBox_esalarytype.addItem("")
        self.comboBox_esalarytype.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_esalarytype, 4, 2, 1, 1)
        self.label_esalary = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_esalary.setObjectName("label_esalary")
        self.gridLayout_4.addWidget(self.label_esalary, 4, 0, 1, 1)
        self.lineEdit_esurname = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_esurname.setText("")
        self.lineEdit_esurname.setObjectName("lineEdit_esurname")
        self.gridLayout_4.addWidget(self.lineEdit_esurname, 1, 1, 1, 2)
        self.label_ename = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_ename.setObjectName("label_ename")
        self.gridLayout_4.addWidget(self.label_ename, 0, 0, 1, 1)
        self.label_ecompany = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_ecompany.setEnabled(False)
        self.label_ecompany.setObjectName("label_ecompany")
        self.gridLayout_4.addWidget(self.label_ecompany, 6, 0, 1, 1)
        self.label_edepartment = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_edepartment.setObjectName("label_edepartment")
        self.gridLayout_4.addWidget(self.label_edepartment, 5, 0, 1, 1)
        self.comboBox_ecompany = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_ecompany.setEnabled(False)
        self.comboBox_ecompany.setEditable(False)
        self.comboBox_ecompany.setDuplicatesEnabled(False)
        self.comboBox_ecompany.setObjectName("comboBox_ecompany")
        self.gridLayout_4.addWidget(self.comboBox_ecompany, 6, 1, 1, 2)
        self.comboBox_edepartment = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_edepartment.setObjectName("comboBox_edepartment")
        self.comboBox_edepartment.addItem("")
        self.comboBox_edepartment.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_edepartment, 5, 1, 1, 2)
        self.lineEdit_ename = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_ename.setText("")
        self.lineEdit_ename.setObjectName("lineEdit_ename")
        self.gridLayout_4.addWidget(self.lineEdit_ename, 0, 1, 1, 2)
        self.doubleSpinBox_esalary = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_esalary.setEnabled(True)
        self.doubleSpinBox_esalary.setMinimumSize(QtCore.QSize(156, 26))
        self.doubleSpinBox_esalary.setSizeIncrement(QtCore.QSize(0, 0))
        self.doubleSpinBox_esalary.setMouseTracking(True)
        self.doubleSpinBox_esalary.setTabletTracking(True)
        self.doubleSpinBox_esalary.setWhatsThis("")
        self.doubleSpinBox_esalary.setAccessibleName("")
        self.doubleSpinBox_esalary.setSpecialValueText("")
        self.doubleSpinBox_esalary.setProperty("showGroupSeparator", False)
        self.doubleSpinBox_esalary.setPrefix("")
        self.doubleSpinBox_esalary.setSuffix("")
        self.doubleSpinBox_esalary.setMaximum(9999999999.0)
        self.doubleSpinBox_esalary.setObjectName("doubleSpinBox_esalary")
        self.gridLayout_4.addWidget(self.doubleSpinBox_esalary, 4, 1, 1, 1)
        self.label_esurname = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_esurname.setObjectName("label_esurname")
        self.gridLayout_4.addWidget(self.label_esurname, 1, 0, 1, 1)
        self.label_email = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_email.setObjectName("label_email")
        self.gridLayout_4.addWidget(self.label_email, 3, 0, 1, 1)
        self.lineEdit_eemail = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_eemail.setObjectName("lineEdit_eemail")
        self.gridLayout_4.addWidget(self.lineEdit_eemail, 3, 1, 1, 2)
        self.label_ephone = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_ephone.setObjectName("label_ephone")
        self.gridLayout_4.addWidget(self.label_ephone, 2, 0, 1, 1)
        self.lineEdit_ephone = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_ephone.setObjectName("lineEdit_ephone")
        self.gridLayout_4.addWidget(self.lineEdit_ephone, 2, 1, 1, 2)
        self.tabWidget.addTab(self.tab_edit, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 241, 58))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_allproduct = QtWidgets.QLabel(self.layoutWidget2)
        self.label_allproduct.setObjectName("label_allproduct")
        self.gridLayout_5.addWidget(self.label_allproduct, 0, 0, 1, 1)
        self.lineEdit_all = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_all.setReadOnly(True)
        self.lineEdit_all.setObjectName("lineEdit_all")
        self.gridLayout_5.addWidget(self.lineEdit_all, 0, 1, 1, 1)
        self.label_allproductval = QtWidgets.QLabel(self.layoutWidget2)
        self.label_allproductval.setObjectName("label_allproductval")
        self.gridLayout_5.addWidget(self.label_allproductval, 1, 0, 1, 1)
        self.lineEdit_allval = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_allval.setReadOnly(True)
        self.lineEdit_allval.setObjectName("lineEdit_allval")
        self.gridLayout_5.addWidget(self.lineEdit_allval, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1209, 22))
        self.menubar.setObjectName("menubar")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHakk_nda = QtWidgets.QAction(MainWindow)
        self.actionHakk_nda.setObjectName("actionHakk_nda")
        self.menuYard_m.addAction(self.actionHakk_nda)
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox_searchtype.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)
        self.comboBox_company.setCurrentIndex(-1)
        self.comboBox_department.setCurrentIndex(-1)
        self.comboBox_ecompany.setCurrentIndex(-1)
        self.comboBox_edepartment.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_name, self.doubleSpinBox_salary)
        MainWindow.setTabOrder(self.doubleSpinBox_salary, self.comboBox_salarytype)
        MainWindow.setTabOrder(self.comboBox_salarytype, self.pushButton_add)
        MainWindow.setTabOrder(self.pushButton_add, self.pushButton_remove)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SelCan - Staff"))
        self.lineEdit_searchval.setWhatsThis(_translate("MainWindow", "Aranacak De??er"))
        self.tableWidget.setAccessibleDescription(_translate("MainWindow", "odta??ta??"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Surname"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Salary"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Department"))
        self.comboBox_searchtype.setItemText(0, _translate("MainWindow", "ID"))
        self.comboBox_searchtype.setItemText(1, _translate("MainWindow", "Name"))
        self.comboBox_searchtype.setItemText(2, _translate("MainWindow", "Salary"))
        self.pushButton_search.setText(_translate("MainWindow", "Search"))
        self.pushButton_reload.setText(_translate("MainWindow", "Reload"))
        self.pushButton_add.setText(_translate("MainWindow", "Add"))
        self.comboBox_salarytype.setItemText(0, _translate("MainWindow", "??? - T??rk Liras??"))
        self.comboBox_salarytype.setItemText(1, _translate("MainWindow", "??? - Euro"))
        self.comboBox_salarytype.setItemText(2, _translate("MainWindow", "$ - Dolar"))
        self.label_salary.setText(_translate("MainWindow", "Salary"))
        self.lineEdit_surname.setPlaceholderText(_translate("MainWindow", "Staff Surname"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.label_company.setText(_translate("MainWindow", "Company"))
        self.label_department.setText(_translate("MainWindow", "Department"))
        self.comboBox_department.setItemText(0, _translate("MainWindow", "Muhasebe"))
        self.comboBox_department.setItemText(1, _translate("MainWindow", "Y??netim"))
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", "Staff Name"))
        self.label_surname.setText(_translate("MainWindow", "Surname"))
        self.label_mail.setText(_translate("MainWindow", "Email"))
        self.lineEdit_email.setPlaceholderText(_translate("MainWindow", "Staff Email"))
        self.label_phone.setText(_translate("MainWindow", "Phone"))
        self.lineEdit_phone.setPlaceholderText(_translate("MainWindow", "Staff Phone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_add), _translate("MainWindow", "Add"))
        self.lineEdit_rmail.setPlaceholderText(_translate("MainWindow", "Staff Email"))
        self.lineEdit_rsalary.setPlaceholderText(_translate("MainWindow", "Staff Salary"))
        self.label_rname.setText(_translate("MainWindow", "Name"))
        self.radioButton_rsure.setText(_translate("MainWindow", "Are you sure?"))
        self.lineEdit_rphone.setPlaceholderText(_translate("MainWindow", "Staff Phone"))
        self.pushButton_remove.setText(_translate("MainWindow", "Remove"))
        self.lineEdit_rid.setPlaceholderText(_translate("MainWindow", "Saff Identity"))
        self.label_rmail.setText(_translate("MainWindow", "Email"))
        self.lineEdit_rname.setPlaceholderText(_translate("MainWindow", "Staff Name and Surname"))
        self.label_rsalary.setText(_translate("MainWindow", "Salary"))
        self.label_rid.setText(_translate("MainWindow", "ID"))
        self.label_rphone.setText(_translate("MainWindow", "Phone"))
        self.label_rdepartment.setText(_translate("MainWindow", "Department"))
        self.lineEdit_rdepartment.setPlaceholderText(_translate("MainWindow", "Staff Department"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_remove), _translate("MainWindow", "Remove"))
        self.pushButton_edit.setText(_translate("MainWindow", "Edit"))
        self.comboBox_esalarytype.setItemText(0, _translate("MainWindow", "??? - T??rk Liras??"))
        self.comboBox_esalarytype.setItemText(1, _translate("MainWindow", "??? - Euro"))
        self.comboBox_esalarytype.setItemText(2, _translate("MainWindow", "$ - Dolar"))
        self.label_esalary.setText(_translate("MainWindow", "Salary"))
        self.lineEdit_esurname.setPlaceholderText(_translate("MainWindow", "Staff Surname"))
        self.label_ename.setText(_translate("MainWindow", "Name"))
        self.label_ecompany.setText(_translate("MainWindow", "Company"))
        self.label_edepartment.setText(_translate("MainWindow", "Department"))
        self.comboBox_edepartment.setItemText(0, _translate("MainWindow", "Muhasebe"))
        self.comboBox_edepartment.setItemText(1, _translate("MainWindow", "Y??netim"))
        self.lineEdit_ename.setPlaceholderText(_translate("MainWindow", "Staff Name"))
        self.label_esurname.setText(_translate("MainWindow", "Surname"))
        self.label_email.setText(_translate("MainWindow", "Email"))
        self.lineEdit_eemail.setPlaceholderText(_translate("MainWindow", "Staff Email"))
        self.label_ephone.setText(_translate("MainWindow", "Phone"))
        self.lineEdit_ephone.setPlaceholderText(_translate("MainWindow", "Staff Phone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_edit), _translate("MainWindow", "Edit"))
        self.label_allproduct.setText(_translate("MainWindow", "Toplam Eleman Say??s??"))
        self.label_allproductval.setText(_translate("MainWindow", "Toplam Maa?? Miktar??"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Info"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Help"))
        self.actionHakk_nda.setText(_translate("MainWindow", "About"))
