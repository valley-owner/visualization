# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'font.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(490, 309)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 20, 60, 38))
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(65, 40))
        font = QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"#pushButton{\n"
"	padding: 0px;margin:0px;background-color: rgba(0,0,0,0);color:#d2d2d2;\n"
"}\n"
"")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 20, 75, 38))
        self.pushButton_2.setMinimumSize(QSize(0, 38))
        self.pushButton_2.setStyleSheet(u"#pushButton_2{\n"
"	background-color: #1E9FFF;\n"
"	border-radius: 19px;\n"
"    border: 1px solid transparent;\n"
"	color: #fff;\n"
"}\n"
"#pushButton_2:hover{\n"
"	background-color: #1b91e5;\n"
"}\n"
"#pushButton_2:pressed{\n"
"	background-color: #1E9FFF;\n"
"}")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 130, 150, 40))
        self.pushButton_3.setStyleSheet(u"#pushButton_3{\n"
"border: 0px;\n"
"  border-radius: 20px;\n"
"  background: #2ec4b6;\n"
"  color: white;\n"
"  outline: none;\n"
"}\n"
"\n"
"#pushButton_3:hover {\n"
"	background-color: rgb(57, 244, 225);\n"
"   border-bottom-right-radius: 30px;\n"
"   border-top-left-radius: 30px;\n"
"   border-bottom-left-radius: 5px;\n"
"   border-top-right-radius: 5px;\n"
"}\n"
"#pushButton_3:pressed{\n"
"	background: #2ec4b6;\n"
"}")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(220, 120, 100, 40))
        self.pushButton_4.setStyleSheet(u"background-color: #4cc9f0;\n"
"border-radius: 20px;")
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(40, 200, 100, 40))
        self.pushButton_5.setStyleSheet(u"background-color: #009688;\n"
"border-radius: 20px;")
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(150, 200, 100, 40))
        self.pushButton_6.setStyleSheet(u"background-color: #5FB878;\n"
"border-radius: 20px;")
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(270, 200, 100, 40))
        self.pushButton_7.setStyleSheet(u"background-color: #393D49;\n"
"border-radius: 20px;\n"
"color:#fff;")
        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(380, 200, 100, 40))
        self.pushButton_8.setStyleSheet(u"background-color: #1E9FFF;\n"
"border-radius: 20px;")
        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(270, 250, 100, 40))
        self.pushButton_9.setStyleSheet(u"background-color: #01AAED;\n"
"border-radius: 20px;\n"
"color:#fff;")
        self.pushButton_10 = QPushButton(Form)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(10, 250, 100, 40))
        self.pushButton_10.setStyleSheet(u"background-color: #FFB800;\n"
"border-radius: 20px;")
        self.pushButton_11 = QPushButton(Form)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(129, 250, 121, 40))
        self.pushButton_11.setStyleSheet(u"background-color: #FF5722;\n"
"border-radius: 20px;")
        self.pushButton_12 = QPushButton(Form)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(380, 250, 100, 40))
        self.pushButton_12.setStyleSheet(u"background-color: #2F4056;\n"
"border-radius: 20px;\n"
"color: #fff;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u4e3b\u8272\u8c03\u4e4b\u4e00", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u4e00\u822c\u7528\u4e8e\u9009\u4e2d\u72b6\u6001", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u901a\u5e38\u7528\u4e8e\u5bfc\u822a", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u7ecf\u5178\u84dd", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"\u6587\u672c\u94fe\u63a5\u7740\u8272", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"\u6696\u8272\u7cfb", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"\u6bd4\u8f83\u5f15\u4eba\u6ce8\u610f\u7684\u989c\u8272", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"\u4fa7\u8fb9\u8272", None))
    # retranslateUi

