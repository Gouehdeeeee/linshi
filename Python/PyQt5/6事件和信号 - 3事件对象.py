from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()    # 创建一个网格布局的变量；
        x = 0
        y = 0
        # 定义两个固定值
        self.text = f"X: {x}, Y: {y}"  # 创建一个文本的变量，里面写这些内容，后续还需要使用这个变量，所以专门定义一个；
        self.label = QLabel(self.text, self)    # 创建一个窗口内的文本的变量，然后获取text的内容；
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        self.setLayout(grid)
        self.setMouseTracking(True)

        self.setGeometry(1000, 380, 360, 240)
        self.setWindowTitle("基础窗口")
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = f"X: {x}, Y: {y}"
        self.label.setText(text)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
