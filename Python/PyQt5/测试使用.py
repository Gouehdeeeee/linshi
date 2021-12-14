from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QWidget, QTextEdit, QSplitter, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)
        bth1 = QPushButton("按钮1", self)
        bth2 = QPushButton("按钮2", self)
        vbox.addWidget(bth1)
        vbox.addWidget(bth2)

        hbox = QHBoxLayout(self)
        topzuo = QFrame(self)
        topzuo.setLayout(vbox)
        topyou = QTextEdit(self)
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topzuo)
        splitter1.addWidget(topyou)
        hbox.addWidget(splitter1)
        das = QWidget(self)
        das.setLayout(hbox)
        self.setCentralWidget(das)

        self.setGeometry(1000, 380, 360, 240)
        self.setWindowTitle("基础窗口")
        self.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
