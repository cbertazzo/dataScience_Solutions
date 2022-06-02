# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_1sIJUcg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 398)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.011, x2:0.972, y2:0.965909, stop:0.113636 rgba(26, 23, 59, 255), stop:1 rgba(63, 37, 63, 255));\n"
"border-radius: 10px;\n"
"")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 40))
        self.title_bar.setStyleSheet(u"background-color: rgba(85, 85, 127, 20);\n"
"border-bottom:1px solid rgb(122, 104, 136);\n"
"border-radius:none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.frame_titles = QFrame(self.title_bar)
        self.frame_titles.setObjectName(u"frame_titles")
        self.frame_titles.setStyleSheet(u"border-bottom:none;\n"
"border-radius:none;")
        self.frame_titles.setFrameShape(QFrame.NoFrame)
        self.frame_titles.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_titles)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.label_11 = QLabel(self.frame_titles)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(60, 0))
        self.label_11.setMaximumSize(QSize(60, 40))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(193, 193, 193);\n"
"background-color: none;")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.horizontalSpacer_14 = QSpacerItem(634, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)


        self.horizontalLayout.addWidget(self.frame_titles)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMinimumSize(QSize(70, 0))
        self.frame_btns.setMaximumSize(QSize(90, 16777215))
        self.frame_btns.setStyleSheet(u"border-bottom:none;\n"
"border-radius:none;")
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(14, 14))
        self.btn_maximize.setMaximumSize(QSize(14, 14))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	background-color: rgb(190, 190, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(14, 14))
        self.btn_minimize.setMaximumSize(QSize(14, 14))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 255, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(14, 14))
        self.btn_close.setMaximumSize(QSize(14, 14))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 84, 5);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tools = QFrame(self.drop_shadow_frame)
        self.tools.setObjectName(u"tools")
        self.tools.setMinimumSize(QSize(0, 0))
        self.tools.setMaximumSize(QSize(50, 16777215))
        self.tools.setStyleSheet(u"border-radius: 0px;\n"
"background-color: rgb(26, 23, 59);\n"
"border-right:1px solid rgb(122, 104, 136);\n"
"")
        self.tools.setFrameShape(QFrame.StyledPanel)
        self.tools.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.tools)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;\n"
"\n"
"")
        self.content_bar.setFrameShape(QFrame.NoFrame)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.bt_open_folder = QPushButton(self.content_bar)
        self.bt_open_folder.setObjectName(u"bt_open_folder")
        self.bt_open_folder.setGeometry(QRect(60, 50, 100, 23))
        self.bt_open_folder.setMinimumSize(QSize(100, 20))
        self.bt_open_folder.setMaximumSize(QSize(150, 23))
        self.bt_open_folder.setStyleSheet(u"QPushButton {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 11px;\n"
"	background-color: rgb(71, 51, 93);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 11px;\n"
"	background-color: rgb(106, 76, 139);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 11px;\n"
"	border: 1px solid rgb(38, 36, 62);\n"
"	background-color: rgb(71, 51, 93);\n"
"\n"
"}")
        self.le_folder = QLineEdit(self.content_bar)
        self.le_folder.setObjectName(u"le_folder")
        self.le_folder.setGeometry(QRect(60, 90, 500, 30))
        self.le_folder.setMinimumSize(QSize(500, 30))
        self.le_folder.setMaximumSize(QSize(16777215, 23))
        self.le_folder.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(45, 29, 56);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid  rgb(122, 104, 136);\n"
"	border-radius: 15px;\n"
"	padding: 25px;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(67, 62, 108);\n"
"	border: 1px solid rgb(188, 188, 188);\n"
"	color: rgb(197, 197, 197);\n"
"}\n"
"QLineEdit:focus {\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(182, 182, 182);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"")
        self.bt_open_file = QPushButton(self.content_bar)
        self.bt_open_file.setObjectName(u"bt_open_file")
        self.bt_open_file.setGeometry(QRect(60, 140, 100, 23))
        self.bt_open_file.setMinimumSize(QSize(100, 20))
        self.bt_open_file.setMaximumSize(QSize(150, 23))
        self.bt_open_file.setStyleSheet(u"QPushButton {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 11px;\n"
"	background-color: rgb(71, 51, 93);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 11px;\n"
"	background-color: rgb(106, 76, 139);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 11px;\n"
"	border: 1px solid rgb(38, 36, 62);\n"
"	background-color: rgb(71, 51, 93);\n"
"\n"
"}")
        self.le_file = QLineEdit(self.content_bar)
        self.le_file.setObjectName(u"le_file")
        self.le_file.setGeometry(QRect(60, 184, 500, 30))
        self.le_file.setMinimumSize(QSize(500, 30))
        self.le_file.setMaximumSize(QSize(16777215, 23))
        self.le_file.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(45, 29, 56);\n"
"	color: rgb(197, 197, 197);\n"
"	border: 1px solid  rgb(122, 104, 136);\n"
"	border-radius: 15px;\n"
"	padding: 25px;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(67, 62, 108);\n"
"	border: 1px solid rgb(188, 188, 188);\n"
"	color: rgb(197, 197, 197);\n"
"}\n"
"QLineEdit:focus {\n"
"	background-color: rgb(48, 44, 77);\n"
"	color: rgb(182, 182, 182);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"")
        self.bt_load = QPushButton(self.content_bar)
        self.bt_load.setObjectName(u"bt_load")
        self.bt_load.setGeometry(QRect(450, 250, 100, 23))
        self.bt_load.setMinimumSize(QSize(100, 20))
        self.bt_load.setMaximumSize(QSize(150, 23))
        self.bt_load.setStyleSheet(u"QPushButton {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 11px;\n"
"	background-color: rgb(71, 51, 93);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 11px;\n"
"	background-color: rgb(106, 76, 139);\n"
"	border: 1px solid rgb(67, 230, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 11px;\n"
"	border: 1px solid rgb(38, 36, 62);\n"
"	background-color: rgb(71, 51, 93);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.content_bar)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMinimumSize(QSize(0, 30))
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: rgb(17, 15, 38);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"\n"
"border-top:1px solid rgb(122, 104, 136);\n"
"")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#7ac8f8;\">My App</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.bt_open_folder.setText(QCoreApplication.translate("MainWindow", u"Open folder", None))
#if QT_CONFIG(tooltip)
        self.le_folder.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#393939;\">Caminho do arquivo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.le_folder.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.le_folder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:/Users/Likely/Documents/name.xlsx", None))
        self.bt_open_file.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
#if QT_CONFIG(tooltip)
        self.le_file.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#393939;\">Caminho do arquivo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.le_file.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.le_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:/Users/Likely/Documents/name.xlsx", None))
        self.bt_load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
    # retranslateUi

