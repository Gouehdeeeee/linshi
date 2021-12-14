from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(1000, 380, 360, 240)
        self.setWindowTitle("基础窗口")
        self.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
