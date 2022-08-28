import PySide6
import os

from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtWidgets import QWidget, QApplication
from LIb.FontAwesome import FontAwesome
from font_uic import Ui_Form
''' 添加临时变量 '''

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class FontText(QWidget):
    def __init__(self):
        super(FontText, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
        # font_id = QFontDatabase.addApplicationFont("..\\Fonts\\FontAwesome\\fontawesome-webfont.ttf")
        # font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
        # self.font = QFont(font_name, 30)
        # self.ui.pushButton.setFont(self.font)
        # self.ui.pushButton.setText(chr(0xf187))
        # QPushButton()
        self.state = False
        QFontDatabase.addApplicationFont("..\\Fonts\\FontAwesome\\fontawesome-webfont.ttf")
        self.ui.pushButton.setFont(QFont("FontAwesome", 38))
        self.ui.pushButton.setText(FontAwesome.fa_toggle_off)
        self.ui.pushButton.clicked.connect(self.change)

    def change(self):
        if self.state:
            self.ui.pushButton.setText(FontAwesome.fa_toggle_off)
            self.ui.pushButton.setStyleSheet('padding: 0px;margin:0px;background-color: rgba(0,0,0,0);color:#d2d2d2;')   # d2d2d2  1bc8e5
            self.state = False
        else:
            self.ui.pushButton.setText(FontAwesome.fa_toggle_on)
            self.ui.pushButton.setStyleSheet('padding: 0px;margin:0px;background-color: rgba(0,0,0,0);color: #5FB878')  # #5FB878 1E9FFF
            self.state = True



if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = FontText()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出