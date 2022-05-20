# https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.buttonClick)
        button.clicked.connect(lambda: self.buttonClick2(button))

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def buttonClick(self):
        # Button clicked Name
        print(self.sender().text())

    def buttonClick2(self, button):
        # Button clicked Name
        print(button.text())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
