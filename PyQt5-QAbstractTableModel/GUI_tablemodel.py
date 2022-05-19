""" A table view example"""
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QPushButton, QWidget, QTableView, QVBoxLayout, \
    QAbstractItemView
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QColor
import pandas as pd
from datetime import datetime


## add cx_Oracle library and MDB main


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self.df = data
        self._data = data.values
        self.headers = data.columns



    def data(self, index, role):
        ### https://stackoverflow.com/questions/57321588/background-color-a-specific-table-row-given-row-number-for-qabstracttablemodel-i
        # https://www.youtube.com/watch?v=yAu155q9Vsg

        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):  # naming of methods is crucial, because they are a methods of inherited abstract class
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    # allows to set data in table
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data[index.row()][index.column()] = value

            # self.dataChanged(index, role) # predefined QAbstractTableModel function - not needed
            return True

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headers[section]

    def dataChanged(self, i, role):
        """ 
        i is for index
        """
        if role == Qt.DisplayRole:
            print(i)

            pass
        if role == Qt.EditRole:
            print("Data changed")

    # allows to enable, edit or select table
    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


class AbstractTableVisualizer(QWidget):  # QMainWindow
    def __init__(self, data, editable=True):
        super().__init__()  # must be called
        self.title = "Data to commit"
        self.left = 100
        self.top = 80
        self.width = 1024
        self.height = 800
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        # data_dict = {"X" : [1, 2, 3], "Y": [4, 5, 6], "SSO_ID":[7, 'E', 9]}
        # data = pd.DataFrame(data_dict)

        self.btn_commit = QPushButton("Commit")
        self.btn_exit = QPushButton("Close")

        self.table = QTableView()
        self.model = TableModel(data)
        self.table.setSortingEnabled(True)
        if editable == False:
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # makes table Read-Only
        self.table.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.btn_commit)
        layout.addWidget(self.btn_exit)

        self.setLayout(layout)
        self.show()


        self.btn_exit.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    data = pd.DataFrame({'x': range(5),
                         'x²': [i ** 2 for i in range(5)],
                         'x³': [i ** 3 for i in range(5)]
                         })

    ex = AbstractTableVisualizer(data, editable=True)
    sys.exit(app.exec_())
