from PyQt5.QtWidgets import QApplication, QPushButton, QToolTip, QLineEdit, QLabel, QGridLayout, QWidget, QHBoxLayout, QVBoxLayout
# QToolTip是工具提示；QGridLayout是网状布局；QHBoxLayout和QVBoxLayout是水平垂直布局；QLineEdit是行编辑；
from PyQt5.QtGui import QFont   # QFont是字体
import sys


class Window1(QWidget):     # 如果想给界面添加布局的话，需要使用QWidget来继承类，如果使用QMainWindow继承类的话就不能添加布局了(自己理解是这里的)；
    def __init__(self):
        super(Window1, self).__init__()

        self.initUI()

    def initUI(self):
        glt1 = QGridLayout()    # 定义一个网状布局的字符串(或者称为网络)；

        lab1 = QLabel("标签1")
        lab2 = QLabel("标签2")
        lab3 = QLabel("标签3")
        lab4 = QLabel("标签4")
        lab5 = QLabel("标签5")
        # 添加两个label

        let1 = QLineEdit()
        let2 = QLineEdit()
        let3 = QLineEdit()
        let4 = QLineEdit()
        let5 = QLineEdit()
        # 添加两个lineedit；行编辑也就是一个长条，然后里面能写字符串，样子就是填写账号密码的框框；

        glt1.addWidget(lab1, 1, 0)
        glt1.addWidget(let1, 1, 1)

        glt1.addWidget(lab2, 2, 0)
        glt1.addWidget(let2, 2, 1)

        glt1.addWidget(lab3, 3, 0)
        glt1.addWidget(let3, 3, 1)

        glt1.addWidget(lab4, 4, 0)
        glt1.addWidget(let4, 4, 1)

        glt1.addWidget(lab5, 5, 0)
        glt1.addWidget(let5, 5, 1)
        # 这里是网状布局添加小部件的写法；第一个字符串代表label或者lineedit；第二个和第三个字符串代表XY轴的点序号(如果以后看到不理解的话可以自己好好想想)；

        bth1_OK = QPushButton()
        bth1_OK.setFont(QFont("SimSun", 10))  # 给按钮更换字体，这里就使用到字体了；里面括号第一个字符串代表字体类型，第二个字符串代表字体大小；
        bth1_OK.setText("OK")
        bth1_OK.setToolTip("这是一个按钮！")  # 给bth1(QPushButton)设置工具提示，看看就明白了，语义很清晰；
        bth2_Cancel = QPushButton()
        bth2_Cancel.setFont(QFont("SimSun", 10))
        bth2_Cancel.setText("Cancel")
        bth2_Cancel.setToolTip("这是一个按钮！")

        HBox = QHBoxLayout()    # 定义一个水平布局的字符串(或者称为网络)；
        HBox.addStretch(1)      # 这个解读为拉伸因子(反正我是没有明白是什么意思)；
        HBox.addWidget(bth1_OK)
        HBox.addWidget(bth2_Cancel)

        VBox = QVBoxLayout()    # 定义一个水平布局的字符串(或者称为网络)；
        VBox.addStretch(1)
        VBox.addLayout(HBox)

        f1 = QWidget()      # 定义一个控件；
        f1.setLayout(glt1)  # 获得glt1的布局
        VBox.addWidget(f1)  # 全局布局再把其他布局添加到部件
        # 这也就是所谓的嵌套布局；
        self.setLayout(VBox)  # 让全局布局VBox应用或者是加载到窗口；

        QToolTip.setFont(QFont("Microsoft YaHei", 8))  # 给工具提示更换字体，这里就使用到字体了；里面括号第一个字符串代表字体类型，第二个字符串代表字体大小；

        self.setGeometry(1000, 300, 500, 150)
        self.setWindowTitle("一个窗口")
        self.setToolTip("这是一个窗口啊啊啊啊啊啊啊！！")  # 给主界面设置工具提示，看看就明白了，语义很清晰；
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window1()
    sys.exit(app.exec_())
