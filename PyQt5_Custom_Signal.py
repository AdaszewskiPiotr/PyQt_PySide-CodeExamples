# Create-GUI-Applications-with-Python_and_Qt5-Martin_Fitzpatrick[2020]
# page 346

import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):

    message = pyqtSignal(str)  
    value = pyqtSignal(int, str, int)
    another = pyqtSignal(list)  
    onemore = pyqtSignal(dict)  
    anything = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.message.connect(self.custom_slot)
        self.value.connect(self.custom_slot)
        self.another.connect(self.custom_slot)
        self.onemore.connect(self.custom_slot)
        self.anything.connect(self.custom_slot)

        self.message.emit("my message")
        self.value.emit(23, "abc", 1)
        self.another.emit([1, 2, 3, 4, 5])
        self.onemore.emit({"a": 2, "b": 7})
        self.anything.emit(1223)

    def custom_slot(self, a):
        print(a)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()