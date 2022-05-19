from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        layout = QVBoxLayout()

        for n in range(10):
            btn = QPushButton(str(n))
            # SIGNAL: The .pressed signal fires whenever the button is pressed.
            # We connect this to self.my_custom_fn via a lambda to pass in
            # additional data.
            # IMPORTANT: You must pass the additional data in as a named
            # parameter on the lambda to create a new namespace. Otherwise
            # the value of n will be bound to the final value in the parent
            # for loop (always 9)
            btn.pressed.connect(lambda n=n: self.my_custom_fn(n) )

            # Add the button to the layout. It will go to the right by default.
            layout.addWidget(btn)

        # Create a empty widget to hold the layout containing our buttons.
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def my_custom_fn(self, n):
        print("Button %d was clicked" % n)


app = QApplication([])

window = MainWindow()
window.show()
app.exec_()