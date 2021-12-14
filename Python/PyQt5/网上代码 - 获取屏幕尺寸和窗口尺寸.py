import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget, QGroupBox, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.screen_size = QLabel(u'尺寸：', self)
        # 创建一个水平布局
        v_box_screen = QVBoxLayout()
        v_box_screen.addWidget(self.screen_size)

        # 创建一个组件组
        group_screen = QGroupBox('屏幕：', self)
        group_screen.setGeometry(10, 10, 120, 50)
        group_screen.setLayout(v_box_screen)

        self.window_position = QLabel(u'坐标：', self)
        self.window_size = QLabel(u'尺寸：', self)
        # 创建一个水平布局
        v_box_window = QVBoxLayout()
        v_box_window.addWidget(self.window_position)
        v_box_window.addWidget(self.window_size)

        # 创建一个组件组
        group_window = QGroupBox('窗口：', self)
        group_window.setGeometry(10, 70, 120, 80)
        group_window.setLayout(v_box_window)

        self.resize(1077, 585)
        self.setWindowTitle('Simple Window')

        self.information()

    def information(self):
        desktop = QDesktopWidget()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()

        self.screen_size.setText(u'尺寸：' + str(screen_width) + u' * ' + str(screen_height))

    def moveEvent(self, *args, **kwargs):
        """重写移动函数"""
        window_x = self.geometry().x()
        window_y = self.geometry().y()
        self.window_position.setText(u'坐标：' + str(window_x) + u' * ' + str(window_y))

    def resizeEvent(self, *args, **kwargs):
        """重写改变尺寸函数函数"""
        window_width = self.geometry().width()
        window_height = self.geometry().height()
        self.window_size.setText(u'尺寸：' + str(window_width) + u' * ' + str(window_height))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
