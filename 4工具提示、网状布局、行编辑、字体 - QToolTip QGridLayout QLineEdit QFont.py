from PyQt5.QtWidgets import QApplication, QPushButton, QToolTip, QLineEdit, QLabel, QGridLayout, QWidget
# QToolTip是工具提示；QGridLayout是网状布局；QLineEdit是行编辑；
from PyQt5.QtGui import QFont   # QFont是字体
import sys


class Window1(QWidget):     # 如果想给界面添加布局的话，需要使用QWidget来继承类，如果使用QMainWindow继承类的话就不能添加布局了(自己理解是这里的)；
    def __init__(self):
        super(Window1, self).__init__()
        self.bth1 = QPushButton(self)

        self.initUI()

    def initUI(self):
        glt1 = QGridLayout()    # 定义一个网状布局的字符串(或者称为网络)；
        self.setLayout(glt1)    # 让glt1布局应用或者是加载到窗口；

        lab1 = QLabel("标签1")
        lab2 = QLabel("标签2")
        # 添加两个label

        let1 = QLineEdit()
        let2 = QLineEdit()
        # 添加两个lineedit；行编辑也就是一个长条，然后里面能写字符串，样子就是填写账号密码的框框；

        glt1.addWidget(lab1, 1, 0)
        glt1.addWidget(let1, 1, 1)

        glt1.addWidget(lab2, 2, 0)
        glt1.addWidget(let2, 2, 1)
        # 这里是网状布局添加小部件的写法；第一个字符串代表label或者lineedit；第二个和第三个字符串代表XY轴的点序号(如果以后看到不理解的话可以自己好好想想)；

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("一个窗口")
        self.setToolTip("这是一个窗口啊啊啊啊啊啊啊！！")  # 给主界面设置工具提示，看看就明白了，语义很清晰；
        self.show()

        self.bth1.setFont(QFont("SimSun", 10))  # 给按钮更换字体，这里就使用到字体了；里面括号第一个字符串代表字体类型，第二个字符串代表字体大小；
        self.bth1.setText("按钮")
        self.bth1.setToolTip("这是一个按钮！")     # 给bth1(QPushButton)设置工具提示，看看就明白了，语义很清晰；

        QToolTip.setFont(QFont("Microsoft YaHei", 10))  # 给工具提示更换字体，这里就使用到字体了；里面括号第一个字符串代表字体类型，第二个字符串代表字体大小；


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window1()
    sys.exit(app.exec_())
