from PySide6.QtCore import QTimer, QUrl
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow
from login import LoginWindow
from main_gui.main_uic import Ui_MainWindow
from variable import GlobalParams
import sys
import os
import PySide6
import ctypes  # 设置任务栏图标
import warnings

'''由于pyside6中globalPos弃用'''
warnings.filterwarnings("ignore")
''' 添加临时变量 '''
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 创建登录类
        self.loginWindow = LoginWindow(self)
        # 创建ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("images/logo.ico"))
        self.setWindowTitle('ov数据可视化')
        self.hide()

        self.url = os.getcwd() + '/web/index.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(self.url))
        self.setCentralWidget(self.browser)
        '''self.setWindowTitle('装载本地Web页面')
        self.setGeometry(5, 30, 1355, 730)
        url = os.getcwd() + '/test.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)
        '''
        # 设置无边框
        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)  # 设置无边框
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # QtWidgets.QShortcut(QtGui.QKeySequence('Esc', ), self, self.close)
        # 5秒自动关闭
        # self._timer = QTimer(self, timeout=self.show_info)
        # self._timer.setSingleShot(True)  # 只触发一次
        # self._timer.start(1000)

    def show_info(self):
        self.ui.username_text.setText(GlobalParams.username)
        self.ui.email_text.setText(GlobalParams.email)
        self.ui.join_time.setText(GlobalParams.join_time)
        self.ui.login_time.setText(GlobalParams.last_login)

    def keyPressEvent(self, event):  # 重新实现了keyPressEvent()事件处理器。
        # 按住键盘事件
        # 这个事件是PyQt自带的自动运行的，当我修改后，其内容也会自动调用
        # print(event.key(), QtCore.Qt.Key_Escape)
        if event.key() == 81:  # 当我们按住键盘是esc按键时
            self.close()  # 关闭程序


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
