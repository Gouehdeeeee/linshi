from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFrame, QSplitter, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("我在主界面~")

        vbox = QVBoxLayout(self)
        bth_1 = QPushButton("1", self)
        bth_2 = QPushButton("2", self)
        bth_3 = QPushButton("3", self)
        bth_4 = QPushButton("4", self)
        bth_5 = QPushButton("5", self)
        bth_6 = QPushButton("6", self)
        vbox.addWidget(bth_1)
        vbox.addWidget(bth_2)
        vbox.addWidget(bth_3)
        vbox.addWidget(bth_4)
        vbox.addWidget(bth_5)
        vbox.addWidget(bth_6)

        topyou_img_label = QLabel("", self)
        topyou_img_label.setPixmap(QPixmap("./Images/146001282.jpg"))
        topyou_img_label.setScaledContents(True)

        hbox = QHBoxLayout(self)
        topzuo = QFrame(self)
        topzuo.setLayout(vbox)  # 我想实现分割的其中一个界面添加上N个按钮，就需要先创建一个帧，从帧setLayout多个部件的集合才能成功；
        # di = QFrame(self)
        # di.setFrameShape(QFrame.StyledPanel)
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topzuo)
        splitter1.addWidget(topyou_img_label)
        splitter1.setStretchFactor(0, 1)  # setStretchFactor是设置界面的比例；括号第一个字符是代表索引界面，比如现在左边就是索引0，右边就是索引1，第二个字符是占的比例；
        splitter1.setStretchFactor(1, 9)
        # splitter2 = QSplitter(Qt.Vertical)
        # splitter2.addWidget(splitter1)
        # splitter2.addWidget(di)
        hbox.addWidget(splitter1)
        widget = QWidget(self)  # 把QWidget创建一个变量加载到网络，然后获取hbox的布局，然后使用setCentralWidget的方式就能让QMainWindow加入布局了；
        widget.setLayout(hbox)
        self.setCentralWidget(widget)  # 这种方式就能使用布局功能了；
        """(这个要和这一行上面的那一行一起看，一起理解)首先你想在QSplitter分割的其中一个界面添加部件的话，那么需要知道Frame(帧)的概念，一个QFrame占用一
        个分割后的一个窗口，如果想在这个窗口内设置其他控件的话，那么需要留一个Frame(帧)用来让其他部件填充；"""
        """禁用的代码是分割第三个界面的代码，感觉还用不到，但是也不想删，所以就存在这里了"""

        muBar_file_save = QAction(self)
        muBar_file_save.setText("&保存")
        muBar_file_save.setIcon(QIcon("./Icons/保存_save.svg"))

        muBar_file_setting = QAction(self)
        muBar_file_setting.setText("&设置")
        muBar_file_setting.setIcon(QIcon("./Icons/配置_config.svg"))
        muBar_file_setting.setShortcut("Ctrl+U")

        muBar_file_quitAct = QAction(self)  # 这是是引入进来的功能，不是QMainWindow的内置功能，所以需要加入self才能加载到MyWindow这个网络中；
        muBar_file_quitAct.setText("&退出")
        muBar_file_quitAct.setIcon(QIcon("./Icons/退出_logout.svg"))
        muBar_file_quitAct.setShortcut("Ctrl+Q")
        muBar_file_quitAct.triggered.connect(qApp.quit)
        """实现按键退出的时候，引发的目标是外部的功能，而不是QMainWindow内置的功能；"""

        muBar_edit_copy = QAction(self)
        muBar_edit_copy.setText("复制")
        muBar_edit_copy.setShortcut("Ctrl+C")

        muBar_edit_paste = QAction(self)
        muBar_edit_paste.setText("粘贴")
        muBar_edit_paste.setShortcut("Ctrl+V")

        muBar_view_fullscreen = QAction(self)
        muBar_view_fullscreen.setText("&全屏")
        muBar_view_fullscreen.setShortcut("Ctrl+P")
        muBar_view_fullscreen.setCheckable(True)
        muBar_view_fullscreen.triggered.connect(fullscreen)
        """实现按键全屏的时候，引发的目标是QMainWindow内置的功能，所以设定的快捷键直接可以使用；"""

        muBar_help_helpcenter = QAction(self)
        muBar_help_helpcenter.setText("&帮助中心")
        muBar_help_helpcenter.setIcon(QIcon("./Icons/帮助中心_helpcenter.svg"))

        muBar = self.menuBar()  # 使用QMainWindow内置的menuBar的话，那么QMainWindow是父级，直接使用self.menuBar()就行了，因为都在继承的范围内；
        muBar_file = muBar.addMenu("&文件")
        muBar_file.addAction(muBar_file_save)
        muBar_file.addAction(muBar_file_setting)
        muBar_file.addAction(muBar_file_quitAct)
        muBar_edit = muBar.addMenu("&编辑")
        muBar_edit.addAction(muBar_edit_copy)
        muBar_edit.addAction(muBar_edit_paste)
        muBar_view = muBar.addMenu("&视图")
        muBar_view.addAction(muBar_view_fullscreen)
        muBar_help = muBar.addMenu("&帮助")
        muBar_help.addAction(muBar_help_helpcenter)

        toolBar = self.addToolBar("")
        toolBar.addAction(muBar_file_save)
        toolBar.addAction(muBar_file_setting)
        toolBar.addAction(muBar_help_helpcenter)
        toolBar.addAction(muBar_file_quitAct)
        """加入工具栏同样需要使用Action，所以也需要创建Action后，toolbar才能添加action；menubar添加选项也需要先创建好Action才能添加Action；"""

        self.setGeometry(625, 245, 1077, 585)
        self.setWindowTitle("实例01")
        self.setWindowOpacity(1)


def fullscreen(state):
    """这个封装函数是让"切换菜单"切换全屏准备的"""
    if state:
        ex.showFullScreen()  # 全屏显示方法
    else:
        ex.showNormal()  # 正常显示方法


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
