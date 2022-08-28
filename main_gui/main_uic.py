# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(310, 190)
        MainWindow.setStyleSheet(u"margin:0px;\n"
"padding:0px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"margin:0px;\n"
"padding:0px;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.close_win = QPushButton(self.centralwidget)
        self.close_win.setObjectName(u"close_win")
        self.close_win.setStyleSheet(u"margin:0px;\n"
"padding:0px;")

        self.horizontalLayout_3.addWidget(self.close_win)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 2, 1, 2)

        self.username_text = QLabel(self.centralwidget)
        self.username_text.setObjectName(u"username_text")

        self.gridLayout.addWidget(self.username_text, 0, 4, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 1, 1, 3)

        self.email_text = QLabel(self.centralwidget)
        self.email_text.setObjectName(u"email_text")

        self.gridLayout.addWidget(self.email_text, 1, 4, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 2, 3, 1, 1)

        self.join_time = QLabel(self.centralwidget)
        self.join_time.setObjectName(u"join_time")

        self.gridLayout.addWidget(self.join_time, 2, 4, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 3)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 3, 3, 1, 1)

        self.login_time = QLabel(self.centralwidget)
        self.login_time.setObjectName(u"login_time")

        self.gridLayout.addWidget(self.login_time, 3, 4, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 310, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e3b\u7a0b\u5e8f", None))
        self.close_win.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.username_text.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u7bb1", None))
        self.email_text.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c\u65f6\u95f4", None))
        self.join_time.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55\u65f6\u95f4", None))
        self.login_time.setText("")
    # retranslateUi

