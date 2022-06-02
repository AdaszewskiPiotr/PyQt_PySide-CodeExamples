# https://doc.qt.io/qtforpython/tutorials/datavisualize/index.html

import sys
import pandas as pd

from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from main_widget import Widget


def read_data(fname):
    # Read the CSV content
    df = pd.read_csv(fname)

    return df


if __name__ == "__main__":
    data = read_data("titanic.csv")

    # Qt Application
    app = QApplication(sys.argv)

    widget = Widget(data)
    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec())
