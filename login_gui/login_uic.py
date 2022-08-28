# -*- coding: utf-8 -*-

##########################################################################
# Form generated from reading UI file 'login.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
##########################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget)
from login_gui import gui_images_rc


class Ui_login_form(object):
    def setupUi(self, login_form):
        if not login_form.objectName():
            login_form.setObjectName(u"login_form")
        login_form.resize(400, 320)
        login_form.setStyleSheet(u"background-color: rgba(255, 255, 255, 1);\n"
                                 "border-radius: 20px;")
        self.verticalLayout_3 = QVBoxLayout(login_form)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.all_form = QWidget(login_form)
        self.all_form.setObjectName(u"all_form")
        self.all_form.setStyleSheet(u"all_form {\n"
                                    "border-radius:15px\n"
                                    "}")
        self.verticalLayout_5 = QVBoxLayout(self.all_form)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, 15, -1)
        self.horizontalSpacer_33 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_33)

        self.closebutton = QPushButton(self.all_form)
        self.closebutton.setObjectName(u"closebutton")
        self.closebutton.setStyleSheet(
            u"#closebutton{\n"
            "image: url(:/login/images/close_gui.svg);\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            "}\n"
            "#closebutton::hover {\n"
            "	background-color: rgb(228, 255, 255)\n"
            "}")
        self.closebutton.setIconSize(QSize(32, 32))

        self.horizontalLayout_15.addWidget(self.closebutton)

        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_34 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_34)

        self.label_6 = QLabel(self.all_form)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamilies([u"\u96b6\u4e66"])
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_6)

        self.horizontalSpacer_45 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_45)

        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.page = QStackedWidget(self.all_form)
        self.page.setObjectName(u"page")
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.verticalLayout = QVBoxLayout(self.login_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.label = QLabel(self.login_page)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.username = QLineEdit(self.login_page)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(200, 0))
        self.username.setFont(font1)
        self.username.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n"
            "border: none;\n"
            "border-bottom: 2px solid #4FA1D9;\n"
            "outline: none;")

        self.gridLayout_2.addWidget(self.username, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.label_2 = QLabel(self.login_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.password = QLineEdit(self.login_page)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(200, 0))
        self.password.setFont(font1)
        self.password.setCursor(QCursor(Qt.IBeamCursor))
        self.password.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n"
            "border: none;\n"
            "border-bottom: 2px solid #4FA1D9;\n"
            "outline: none;")
        self.password.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.password, 1, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 1, 3, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.login_btn = QPushButton(self.login_page)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(100, 40))
        self.login_btn.setFont(font1)
        self.login_btn.setStyleSheet(u"border-radius: 20px;\n"
                                     "border: 1px solid lightseagreen;\n"
                                     "background: lightseagreen;\n"
                                     "color: #fff;")

        self.gridLayout_3.addWidget(self.login_btn, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.sgin_up_btn = QPushButton(self.login_page)
        self.sgin_up_btn.setObjectName(u"sgin_up_btn")
        self.sgin_up_btn.setMinimumSize(QSize(100, 40))
        self.sgin_up_btn.setFont(font1)
        self.sgin_up_btn.setStyleSheet(u"border-radius: 20px;\n"
                                       "border: 1px solid lightseagreen;\n"
                                       "background: lightseagreen;\n"
                                       "color: #fff;")

        self.gridLayout_3.addWidget(self.sgin_up_btn, 1, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 4, 1, 1)

        self.forget_btn = QPushButton(self.login_page)
        self.forget_btn.setObjectName(u"forget_btn")
        self.forget_btn.setFont(font1)
        self.forget_btn.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n"
            "color: lightseagreen;")

        self.gridLayout_3.addWidget(self.forget_btn, 0, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.page.addWidget(self.login_page)
        self.sgin_up_page = QWidget()
        self.sgin_up_page.setObjectName(u"sgin_up_page")
        self.verticalLayout_2 = QVBoxLayout(self.sgin_up_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_11 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.label_3 = QLabel(self.sgin_up_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)

        self.sgin_username = QLineEdit(self.sgin_up_page)
        self.sgin_username.setObjectName(u"sgin_username")
        self.sgin_username.setMinimumSize(QSize(200, 0))
        self.sgin_username.setFont(font1)
        self.sgin_username.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n"
            "border: none;\n"
            "border-bottom: 2px solid #4FA1D9;\n"
            "outline: none;")
        self.sgin_username.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.sgin_username, 0, 3, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 0, 4, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_13, 1, 0, 1, 1)

        self.label_4 = QLabel(self.sgin_up_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 1, 2, 1, 1)

        self.sgin_emal = QLineEdit(self.sgin_up_page)
        self.sgin_emal.setObjectName(u"sgin_emal")
        self.sgin_emal.setMinimumSize(QSize(200, 0))
        self.sgin_emal.setFont(font1)
        self.sgin_emal.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n"
            "border: none;\n"
            "border-bottom: 2px solid #4FA1D9;\n"
            "outline: none;")
        self.sgin_emal.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.sgin_emal, 1, 3, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_15, 1, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 2, 0, 1, 1)

        self.label_7 = QLabel(self.sgin_up_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_23, 2, 2, 1, 1)

        self.sgin_password = QLineEdit(self.sgin_up_page)
        self.sgin_password.setObjectName(u"sgin_password")
        self.sgin_password.setMinimumSize(QSize(200, 0))
        self.sgin_password.setFont(font1)
        self.sgin_password.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n"
            "border: none;\n"
            "border-bottom: 2px solid #4FA1D9;\n"
            "outline: none;")
        self.sgin_password.setEchoMode(QLineEdit.Password)
        self.sgin_password.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.sgin_password, 2, 3, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_24, 2, 4, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_26, 3, 0, 1, 1)

        self.label_8 = QLabel(self.sgin_up_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_27, 3, 2, 1, 1)

        self.sgin_rpassword = QLineEdit(self.sgin_up_page)
        self.sgin_rpassword.setObjectName(u"sgin_rpassword")
        self.sgin_rpassword.setMinimumSize(QSize(200, 0))
        self.sgin_rpassword.setFont(font1)
        self.sgin_rpassword.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n"
            "border: none;\n"
            "border-bottom: 2px solid #4FA1D9;\n"
            "outline: none;")
        self.sgin_rpassword.setEchoMode(QLineEdit.Password)
        self.sgin_rpassword.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.sgin_rpassword, 3, 3, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_25, 3, 4, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_18, 4, 0, 1, 1)

        self.label_5 = QLabel(self.sgin_up_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_16, 4, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, -1)
        self.ver_code = QLineEdit(self.sgin_up_page)
        self.ver_code.setObjectName(u"ver_code")
        self.ver_code.setMinimumSize(QSize(100, 0))
        self.ver_code.setFont(font1)
        self.ver_code.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n"
            "border: none;\n"
            "border-bottom: 2px solid #4FA1D9;\n"
            "outline: none;")
        self.ver_code.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.ver_code)

        self.ver_code_btn = QPushButton(self.sgin_up_page)
        self.ver_code_btn.setObjectName(u"ver_code_btn")
        self.ver_code_btn.setMinimumSize(QSize(100, 30))
        self.ver_code_btn.setFont(font1)
        self.ver_code_btn.setStyleSheet(u"border-radius: 10px;\n"
                                        "color: #FFF;\n"
                                        "background: lightseagreen;\n"
                                        "border-color: lightseagreen;")

        self.horizontalLayout.addWidget(self.ver_code_btn)

        self.gridLayout.addLayout(self.horizontalLayout, 4, 3, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_21, 4, 4, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_20 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_20)

        self.login_page_btn = QPushButton(self.sgin_up_page)
        self.login_page_btn.setObjectName(u"login_page_btn")
        self.login_page_btn.setMinimumSize(QSize(100, 40))
        self.login_page_btn.setFont(font1)
        self.login_page_btn.setStyleSheet(u"border-radius: 20px;\n"
                                          "border: 1px solid lightseagreen;\n"
                                          "background: lightseagreen;\n"
                                          "color: #fff;")

        self.horizontalLayout_5.addWidget(self.login_page_btn)

        self.horizontalSpacer_19 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_19)

        self.sgin_up = QPushButton(self.sgin_up_page)
        self.sgin_up.setObjectName(u"sgin_up")
        self.sgin_up.setMinimumSize(QSize(100, 40))
        self.sgin_up.setFont(font1)
        self.sgin_up.setStyleSheet(u"border-radius: 20px;\n"
                                   "border: 1px solid lightseagreen;\n"
                                   "background: lightseagreen;\n"
                                   "color: #fff;")

        self.horizontalLayout_5.addWidget(self.sgin_up)

        self.horizontalSpacer_22 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_22)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.page.addWidget(self.sgin_up_page)

        self.verticalLayout_5.addWidget(self.page)

        self.verticalLayout_3.addWidget(self.all_form)

        self.retranslateUi(login_form)

        self.page.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(login_form)
    # setupUi

    def retranslateUi(self, login_form):
        login_form.setWindowTitle(
            QCoreApplication.translate(
                "login_form", u"Form", None))
        self.closebutton.setText("")
        self.label_6.setText(
            QCoreApplication.translate(
                "login_form",
                u"\u6b22\u8fce\u4f7f\u7528\uff01\uff01\uff01",
                None))
        self.label.setText(
            QCoreApplication.translate(
                "login_form",
                u"\u8d26     \u53f7     \uff1a",
                None))
        self.username.setPlaceholderText(QCoreApplication.translate(
            "login_form", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.label_2.setText(
            QCoreApplication.translate(
                "login_form",
                u"\u5bc6     \u7801     \uff1a",
                None))
        self.password.setPlaceholderText(QCoreApplication.translate(
            "login_form", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.login_btn.setText(
            QCoreApplication.translate(
                "login_form", u"\u767b\u5f55", None))
        self.sgin_up_btn.setText(
            QCoreApplication.translate(
                "login_form", u"\u6ce8\u518c", None))
        self.forget_btn.setText(
            QCoreApplication.translate(
                "login_form",
                u"\u5fd8\u8bb0\u5bc6\u7801",
                None))
        self.label_3.setText(
            QCoreApplication.translate(
                "login_form",
                u"\u7528\u6237\u540d",
                None))
        self.sgin_username.setPlaceholderText(QCoreApplication.translate(
            "login_form", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.label_4.setText(
            QCoreApplication.translate(
                "login_form",
                u"\u90ae\u7bb1",
                None))
        self.sgin_emal.setPlaceholderText(QCoreApplication.translate(
            "login_form", u"\u8bf7\u8f93\u5165\u90ae\u7bb1", None))
        self.label_7.setText(
            QCoreApplication.translate(
                "login_form",
                u"\u5bc6\u7801",
                None))
        self.sgin_password.setPlaceholderText(QCoreApplication.translate(
            "login_form", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.label_8.setText(
            QCoreApplication.translate(
                "login_form",
                u"\u91cd\u590d\u5bc6\u7801",
                None))
        self.sgin_rpassword.setPlaceholderText(QCoreApplication.translate(
            "login_form", u"\u8bf7\u518d\u6b21\u8f93\u5165\u5bc6\u7801", None))
        self.label_5.setText(
            QCoreApplication.translate(
                "login_form",
                u"\u9a8c\u8bc1\u7801",
                None))
        self.ver_code.setPlaceholderText(QCoreApplication.translate(
            "login_form", u"\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801", None))
        self.ver_code_btn.setText(
            QCoreApplication.translate(
                "login_form",
                u"\u83b7\u53d6\u9a8c\u8bc1\u7801",
                None))
        self.login_page_btn.setText(
            QCoreApplication.translate(
                "login_form", u"\u767b\u5f55", None))
        self.sgin_up.setText(
            QCoreApplication.translate(
                "login_form",
                u"\u6ce8\u518c",
                None))
    # retranslateUi
