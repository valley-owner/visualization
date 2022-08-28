import time

import PySide6
import os
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QGraphicsDropShadowEffect
from PySide6.QtGui import Qt, QBitmap, QPainter, QIcon, QColor
from PySide6 import QtCore
# from gui.login_uic import Ui_login_form
import variable
from login_gui.login_uic import Ui_login_form
from db_sql.login_sql import Data
import random

'''由于pyside6中globalPos弃用'''
import re
from until.get_path import get_project_path
from until.make_password import make_pkw

##########################################################
''' 添加临时变量 '''

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

##########################################################


logs = os.path.exists('db')
if not logs:
    os.mkdir('db')

if not os.path.exists(get_project_path() + '\\db\\date.db'):
    Db = Data()
    Db.create_user_table()


class LoginWindow(QWidget):
    def __init__(self, main_window=None):
        super(LoginWindow, self).__init__()
        # 保存好父窗口，用于登录后显示父窗口
        self.parent = main_window
        # 创建ui
        self.Point = None
        self.Move = None
        self.ui = Ui_login_form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("images/logo.ico"))
        # flags=Qt.FramelessWindowHint
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)  # 设置无边框
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.bmp = QBitmap(400, 320)  # 这里将window size引入，否则无效果！
        self.bmp.fill()
        self.Painter = QPainter(self.bmp)
        self.Painter.setPen(Qt.NoPen)
        self.Painter.setBrush(Qt.black)
        self.Painter.drawRoundedRect(self.bmp.rect(), 30, 30)  # 倒边角为15px
        self.setMask(self.bmp)  # 切记将self.bmp Mark到window
        self.ui.page.setCurrentIndex(0)
        # 显示自己
        self.show()
        self.bind()

        # # 边框阴影
        # effect = QGraphicsDropShadowEffect(self)
        # effect.setBlurRadius(1)
        # effect.setColor(QColor(0, 0, 0, 1))
        # effect.setOffset(0, 1)
        # self.setGraphicsEffect(effect)
        # self.adjustSize()
        self.code_num = None

    def bind(self):
        self.ui.login_btn.clicked.connect(self.login)  # 登录
        self.ui.closebutton.clicked.connect(self.login_close)  # 关闭
        self.ui.forget_btn.clicked.connect(self.forget)  # 忘记密码
        self.ui.sgin_up_btn.clicked.connect(
            lambda: self.change_page(1))  # 切换到注册页面
        self.ui.login_page_btn.clicked.connect(
            lambda: self.change_page(0))  # 切换到登录页面
        self.ui.sgin_up.clicked.connect(self.sgin_up)  # 登录
        self.ui.username.editingFinished.connect(
            lambda: self.check_username(self.ui.username.text()))  # 用户名输入完成
        self.ui.password.editingFinished.connect(
            lambda: self.check_username(self.ui.password.text()))  # 用户名输入完成
        self.ui.sgin_username.editingFinished.connect(
            lambda: self.check_username(self.ui.sgin_username.text(), typ='register'))  # 注册用户名填写完成
        self.ui.sgin_password.editingFinished.connect(
            lambda: self.check_password(self.ui.sgin_password.text(), typ='register'))  # 注册密码填写完成
        self.ui.sgin_emal.editingFinished.connect(
            lambda: self.check_email(self.ui.sgin_emal.text(), typ='register'))  # 注册邮箱填写完成
        self.ui.sgin_rpassword.editingFinished.connect(self.check_r_password)
        self.ui.ver_code_btn.clicked.connect(self.ver_code)

    def check_r_password(self):
        password = self.ui.sgin_password.text()
        r_password = self.ui.sgin_rpassword.text()
        if not self.check_password(r_password):
            return
        if password != r_password:
            QMessageBox.warning(self, '参数错误', '两次输入密码不一致！！！')

    def set_focus_username_typ(self, typ):
        if typ == 'login':
            self.ui.username.setFocus()
        else:
            self.ui.sgin_username.setFocus()

    def set_focus_password_typ(self, typ):
        if typ == 'login':
            self.ui.password.setFocus()
        else:
            self.ui.sgin_password.setFocus()

    def set_focus_email_typ(self, typ):
        # if typ == 'login':
        self.ui.sgin_emal.setFocus()
        # else:
        #     self.ui.sgin_password.setFocus()

    def check_username(self, username, typ='login'):
        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username):
            QMessageBox.warning(self, '参数错误', '请输入5-20个字符的用户名，只能含有数字和字母！！！')
            self.set_focus_username_typ(typ)
            return False
        # 查询数据库中是否含有该用户名 有返回1 无返回0
        return True

    def check_email(self, email, typ='login'):
        if not re.match(
            r'^[a-z0-9][\w\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',
                email):
            QMessageBox.warning(self, '参数错误', '邮箱格式错误！！！')
            self.set_focus_email_typ(typ)
            return False
        return True

    def check_password(self, password, typ='login'):
        if len(password) < 6:
            QMessageBox.warning(self, '参数错误', '密码长度应该大于6位，否则密码强度不足！！！')
            self.set_focus_password_typ(typ)
            return False
        return True

    # 登录事件
    def login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        if not self.check_username(username):
            return
        if not self.check_password(password):
            return
        data = Data()
        user = data.select_user(username)
        pkw = make_pkw(username, password)
        try:
            if pkw not in user:
                QMessageBox.warning(self, '登录出错', '请检查密码是否正确')
                return
        except TypeError:
            QMessageBox.warning(self, '登录出错', '用户不存在！！！')
            return
        user_data = Data()
        user_data.update_user(username)
        variable.GlobalParams.username = username
        variable.GlobalParams.email = user[2]
        variable.GlobalParams.join_time = user[4]
        variable.GlobalParams.last_login = str(time.strftime('%Y-%m-%d %H:%M:%S'))
        self.parent.showMaximized()
        self.parent.show()
        self.close()

    # 关闭程序
    def login_close(self):
        self.close()

    # 忘记密码
    def forget(self):
        QMessageBox.information(self, '找回密码', '抱歉目前还不支持找回密码，可以联系作者找回')

    # 切换页面
    def change_page(self, page):
        self.ui.page.setCurrentIndex(int(page))

    # 注册
    def sgin_up(self):
        username = self.ui.sgin_username.text()
        email = self.ui.sgin_emal.text()
        password = self.ui.sgin_password.text()
        r_password = self.ui.sgin_rpassword.text()
        ver_code = self.ui.ver_code.text()
        if not self.check_username(username):
            return
        if not self.check_email(email):
            return
        if not self.check_password(password):
            return
        if not self.check_password(r_password):
            return
        if password != r_password:
            QMessageBox.warning(self, '参数错误', '两次输入密码不一致！！！')
            return
        if int(ver_code) != self.code_num:
            QMessageBox.warning(self, '参数错误', '验证码错误，请认真检查！！！')
            return
        # sql_email = email.replace('@', '100')
        pwk = make_pkw(username, password)
        user_data = Data()
        if user_data.select_user(username) is not None:
            QMessageBox.warning(self, '注册出错', '该用户名已经存在！！！')
            return
        user = Data()
        user.insert_user(username, email, pwk, join_time=str(time.strftime('%Y-%m-%d %H:%M:%S')))
        QMessageBox.information(self, '注册成功', '恭喜您注册成功')
        self.change_page(0)

    def ver_code(self):
        self.code_num = random.randint(1000, 9999)
        print(self.code_num)

    def mousePressEvent(self, event):  # 事件开始
        if event.button() == QtCore.Qt.LeftButton:
            self.Move = True  # 设定bool为True
            self.Point = event.globalPos() - self.pos()  # 记录起始点坐标
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):  # 移动时间
        if QtCore.Qt.LeftButton and self.Move:  # 切记这里的条件不能写死，只要判断move和鼠标执行即可！
            self.move(QMouseEvent.globalPos() - self.Point)  # 移动到鼠标到达的坐标点！
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 结束事件
        self.Move = False


if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = LoginWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出
