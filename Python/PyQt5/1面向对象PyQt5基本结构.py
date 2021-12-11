from PyQt5.QtWidgets import QApplication, QMainWindow   # QApplication是创建基础窗口的对象；QMainWindow是创建基础窗口；


class MyWindow(QMainWindow):    # 创建”类“MyWindow继承自QMainWindow；
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
        # 基础的面向对象编程写法，不知道什么意思；

    def initUI(self):   # 这个封装函数应该是专门写UI代码的地方
        self.setGeometry(300, 300, 360, 240)
        self.setWindowTitle("基础窗口")
        self.move(100, 100)
        self.show()
        # 基础窗口设置四个步骤


if __name__ == "__main__":
    import sys  # 自己理解这个是导入循环命令
    app = QApplication(sys.argv)    # 创建一个应用对象
    ex = MyWindow()     # 按这里类创建一个实例
    sys.exit(app.exec_())   # 退出循环命令集
