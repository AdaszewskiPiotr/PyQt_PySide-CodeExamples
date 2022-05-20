"""Dosctring of the Module."""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    """Docstring of the Class."""

    def __init__(self):
        super().__init__()
        self.title = 'My App'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        """Docstring of the Method."""
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tab1 = Tab1Widget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(self.tab1, self.tab1.title)
        self.tabWidget.addTab(self.tab2, "Tab 2")
        self.tabWidget.addTab(self.tab3, "Tab 3")

        # Set the central widget of the Window.
        self.setCentralWidget(self.tabWidget)

        self.show()


class Tab1Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Title here'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())
