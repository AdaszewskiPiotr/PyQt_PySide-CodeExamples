# Create-GUI-Applications-with-Python_and_Qt5-Martin_Fitzpatrick[2020]
# page 136

import sys

from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow,
                             QPushButton, QVBoxLayout, QWidget)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.w = None
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        # Check whether the window has already being created before creating it
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w = None   # Discard reference, close window.


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
