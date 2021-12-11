from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton  # QLabel在窗口内创建文本；QPushButton在窗口内创建按钮；
from PyQt5.QtGui import QIcon   # 创建窗口图标；


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.lab1 = QLabel(self)    # 创建lab1对象，创建这些一定要在self.initUI()的上面创建，不然会报错；
        self.bth1 = QPushButton(self)   # 创建bth1对象，创建这些一定要在self.initUI()的上面创建，不然会报错；

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 350)
        self.setWindowTitle("简单窗口")
        self.setWindowIcon(QIcon("./Icons/奶瓶_bottle.svg"))  # 在主窗口创建图标的写法；
        self.show()

        #self.lab1.setText("Hello World！")
        #self.lab1.move(50, 50)
        # 上面两行是QLabel简单使用的写法；
        self.lab1.setText("<a href='https://iconpark.oceanengine.com/official' style='color:blue'>图标网站</a>")
        # 这一行是创建超链接的写法，语义非常明确，可以自己看；
        self.lab1.setOpenExternalLinks(True)    # 超链接创建后，需要加入这一行命令才能使这个链接能打开；
        self.lab1.move(50, 50)  # 基本移动

        self.bth1.setText("按钮")     # 按钮显示的文字；
        self.bth1.setIcon(QIcon("./Icons/心电_cardioelectric.svg"))   # 按钮前面显示的图标的写法；
        self.bth1.move(20, 0)   # 基本移动


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
