from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QDialog    # QMessageBox是消息盒子；
# 这里想实现两个窗口之间跳转，然后在子窗口里面创建弹出窗口，使用的是QMainWindow和QDialog实现；
# ！！！它们都不能继承两次，意思就是说，QMainWindow不能继承两个类，不然会出错！！！(特指QMainWindow和QDialog)
# QMainWindow、QDialog、QWidget区别和选择，下面说：
# QMainWindow类提供一个有菜单条、锚接窗口（例如工具条）和一个状态条的主应用程序窗口；
# QWidget类是所有用户界面对象的基类；
# QDialog是最普通的顶级窗口；
import sys
from PyQt5.QtGui import QIcon


class Window2(QDialog):     # 这里定义一个类，这个类以后使用到副窗口(自己是这样理解的)；
    # ！！！它们都不能继承两次，意思就是说，QMainWindow不能继承两个类，不然会出错！！！(特指QMainWindow和QDialog)
    def __init__(self):
        super(Window2, self).__init__()
        self.bth1_2 = QPushButton(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("副窗口")
        self.setGeometry(450, 450, 400, 350)
        self.show()

        self.bth1_2.setText("窗口二按钮")
        self.bth1_2.resize(100, 30)
        self.bth1_2.clicked.connect(self.Mes_2)     # 这里按下按钮之后信号会传递到Mes_2，而Mes_2的功能就是消息盒子(自己是这样理解的)；

    def Mes_2(self):
        QMessageBox.about(self, "我是弹出窗口", "哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈！！！")
        # 封装一个函数，这个函数里面使用消息盒子，之后让Window2窗口的bth1_2按钮调用；括号中的第二段字符串代表“窗口的title”，第三段字符串代表“窗口中的label”


class Window1(QMainWindow):     # 这里定义一个类，这个类是用作主窗口(自己是这样理解的)；
    # ！！！它们都不能继承两次，意思就是说，QMainWindow不能继承两个类，不然会出错！！！(特指QMainWindow和QDialog)
    def __init__(self):
        super(Window1, self).__init__()
        self.bth1_1 = QPushButton(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("主窗口")
        self.setGeometry(350, 350, 400, 350)
        self.show()

        self.bth1_1.setText("<---比个腰子")
        self.bth1_1.setIcon(QIcon("./Icons/腹部_abdominal.svg"))
        self.bth1_1.resize(150, 30)
        self.bth1_1.clicked.connect(self.NewWindow)

    def NewWindow(self):    # 这里封装一个函数，这里函数的作用是把Window2进来然后让主窗口的按钮调用；
        new_win = Window2()     # 这里是代表实例化Window2，因为Window2只是一个类，不能直接使用；
        new_win.show()          # 显示这个实例；
        new_win.exec_()         # 退出循环这个实例；


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window1()
    sys.exit(app.exec_())
