from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
# QAction是动作的意思，在本项目中是用于添加子级选项；qApp是基类窗口的各种操作，本项目中用于引发退出功能(自己是这样理解的)；QMenu是菜单，项目使用这个创建子级菜单栏和右键上下文菜单；
from PyQt5.QtGui import QIcon
import sys


class Example(QMainWindow):     # 这个需要继承自QMainWindow；
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready")   # 创建一个状态栏，并在APP开启的时候在状态栏显示括号里面的文本；

        # exitAct = QAction(QIcon('exit.png'), '&Exit', self)    # 组合写法，括号第一代表改图标，第二代表文本，第三代表加载到整个视图网络(其他的也可以参考这个格式)；
        filemu_exitact = QAction(self)  # 实例化一个对象，使用QAction创建一个子级选项；
        filemu_exitact.setIcon(QIcon("./Icons/退出_logout.svg"))  # 给子级选项添加图标；
        filemu_exitact.setText("&Exit")     # 给子级选项添加名称(我不知道为什么添加的选项名称的时候前面添加了&，我也不知道，添加就好了)；
        filemu_exitact.setShortcut("Ctrl+Q")    # 给子级选项添加快捷键，并能把快捷键显示在选项后面；
        filemu_exitact.setStatusTip("退出APP")    # 给子级选项添加状态栏提示；
        filemu_exitact.triggered.connect(qApp.quit)     # 按下这个选项后引发事件，比如这个按钮现在的意思是退出，那么按下选项后就引发退出信号；

        filemu_RecentlyUse = QMenu(self)    # 实例化一个对象，使用QMenu创建一个子级菜单栏；
        filemu_RecentlyUse.setTitle("Recently Use")     # 创建的子级菜单栏需要使用setTitle才能添加名称；

        filemu_RecentlyUse_file = QAction(self)     # 实例化一个对象，使用QAction创建用于子级菜单的子级选项；
        filemu_RecentlyUse_file.setText("...")      # 添加名称；
        filemu_RecentlyUse_file.setStatusTip("........................")    # 添加状态栏提示；

        filemu_RecentlyUse.addAction(filemu_RecentlyUse_file)   # 这一步是把子级菜单的子级选项加入到子级菜单中；

        editmu_copyact = QAction(self)
        editmu_copyact.setText("&Copy")
        editmu_copyact.setShortcut("Ctrl+C")
        editmu_copyact.setStatusTip("Copy this")

        viewmu_hidestatusbar = QAction(self)    # 实例化一个对象，使用QAction创建一个子级选项；
        viewmu_hidestatusbar.setText("Hide the statusBar")
        viewmu_hidestatusbar.setStatusTip("勾选之后就把状态栏隐藏了！！！；")
        viewmu_hidestatusbar.setShortcut("Ctrl+W")
        viewmu_hidestatusbar.setCheckable(True)     # 这个写法是把选项改成切换式选项了，变成可以勾选或者取消勾选的选项，括号里面是真或假的条件；
        viewmu_hidestatusbar.triggered.connect(self.togglemenu_statusbarstatu)
        # 选项引发事件，这里实现的是勾选后状态栏隐藏，取消勾选是状态栏显示，关联的封装函数是togglemenu；

        filemu_exitact_toolbar = self.addToolBar("Exit")  # 实例化这个属性，括号里面的意义不明，填写其他的在图形界面上看不出来差别
        filemu_exitact_toolbar.addAction(filemu_exitact)

        self.statusBar()    # 对象应用到窗口视图；

        mubar = self.menuBar()  # 实例化一个对象，使用继承过来的QMenuBar来创建顶级菜单栏(自己是这样理解的)；
        filemu = mubar.addMenu("&File")     # 添加名称；
        filemu.addMenu(filemu_RecentlyUse)  # 添加子级菜单栏；
        filemu.addMenu(filemu_RecentlyUse).setStatusTip("最近使用的文件列表")    # 添加子级菜单栏的状态栏提示；！！！必须要是在这里设置状态栏才不会出错；
        filemu.addAction(filemu_exitact)    # 添加选项

        editmu = mubar.addMenu("&Edit")
        editmu.addAction(editmu_copyact)

        viewmu = mubar.addMenu("&View")
        viewmu.addAction(viewmu_hidestatusbar)

        self.setGeometry(1000, 300, 500, 420)
        self.setWindowTitle("创建状态栏、工具栏、菜单栏、右键上下文菜单栏")
        self.show()

    def togglemenu_statusbarstatu(self, state):    # 这里要达到True就是隐藏状态栏，Falsh就是显示状态栏的目的，封装的togglemenu函数，以state为判断依据，这个非常重要！
        if state:
            self.statusBar().hide()
        else:
            self.statusBar().show()

    def contextMenuEvent(self, event):  # 这里要达到右键上下文菜单栏的目的，封装的contextMenuEvent函数，以event为判断依据，这个非常重要！
        youjianmenu = QMenu(self)
        newAct = youjianmenu.addAction("New")
        openAct = youjianmenu.addAction("Open")
        quitAct = youjianmenu.addAction("Quit")
        # 创建三个选项；
        action = youjianmenu.exec_(self.mapToGlobal(event.pos()))   # 这个应该是右键上下文的关键代码(这个还需要深入了解)；
        if action == quitAct:
            qApp.quit()
        # 这个判断语义看起来很明确，action(行为)如果等于quitAct这个变量的话，那么用户按下quit选项后就会发生qApp.quit()，使APP退出；


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
