# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kaninym/PycharmProjects/SelCan/Window/ui/LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(843, 663)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/kaninym/PycharmProjects/SelCan/Window/ui/../logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.setWindowIcon(icon)
        window.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_pass.setObjectName("label_pass")
        self.gridLayout.addWidget(self.label_pass, 7, 0, 1, 1)
        self.label_uname = QtWidgets.QLabel(self.centralwidget)
        self.label_uname.setObjectName("label_uname")
        self.gridLayout.addWidget(self.label_uname, 6, 0, 1, 1)
        self.line_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.line_pass.setDragEnabled(False)
        self.line_pass.setObjectName("line_pass")
        self.gridLayout.addWidget(self.line_pass, 7, 1, 1, 1)
        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setObjectName("button_login")
        self.gridLayout.addWidget(self.button_login, 8, 0, 1, 2)
        self.line_uname = QtWidgets.QLineEdit(self.centralwidget)
        self.line_uname.setObjectName("line_uname")
        self.gridLayout.addWidget(self.line_uname, 6, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(200, 200))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/home/kaninym/PycharmProjects/SelCan/Window/ui/../logo3.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 5, 3, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(300, 300))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("/home/kaninym/PycharmProjects/SelCan/Window/ui/../logo2.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(300, 300))
        self.label.setMaximumSize(QtCore.QSize(300, 300))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/kaninym/PycharmProjects/SelCan/Window/ui/../logo.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 3, 1, 1)
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 22))
        self.menubar.setObjectName("menubar")
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "SelCan - Login"))
        self.label_pass.setText(_translate("window", "Password"))
        self.label_uname.setText(_translate("window", "Username"))
        self.button_login.setText(_translate("window", "Login"))