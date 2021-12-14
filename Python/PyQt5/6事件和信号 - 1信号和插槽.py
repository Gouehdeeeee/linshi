import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLCDNumber, QSlider     # QLCDNumber是显示会变化的数字；QSlider是滑块控件；


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        shuzixianshi = QLCDNumber(self)
        huakuai = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(shuzixianshi)
        vbox.addWidget(huakuai)
        self.setLayout(vbox)

        huakuai.valueChanged.connect(shuzixianshi.display)  # 在这里，我们将滑块的信号连接到数字的插槽。发送方是发送信号的对象。接收器是接收信号的对象。插槽是对信号做出反应的方法；
        # 发送方是发送信号的对象。接收器是接收信号的对象。插槽是对信号做出反应的方法。

        self.setGeometry(1000, 300 ,500 ,350)
        self.setWindowTitle("窗口")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
