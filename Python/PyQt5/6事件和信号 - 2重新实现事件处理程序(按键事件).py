from PyQt5.QtCore import Qt     # 使用键盘关闭窗口
from PyQt5.QtWidgets import QApplication, QWidget


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1000, 380, 360, 240)
        self.setWindowTitle("基础窗口")
        self.show()

    def keyPressEvent(self, e):
        """def后面的封装函数还不能变，不然会出现问题。导致下面无法通过键盘关闭窗口"""
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
