import sys
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

'''
https://learndataanalysis.org/display-pandas-dataframe-with-pyqt5-qtableview-widget/
It reacts to the changing columns quantity
'''

df = pd.DataFrame({'a': ['Mary', 'Jim', 'John', 'test'],
                   'b': [100, 200, 300, 500],
                   'c': ['a', 'b', 'c', 'ads'],
                   'd': ['a', 'b', 'c', 'ads']})


class PandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def setData(self, index, value, role):
        if not value.isdigit():                                               # +++
            return False                                                      # +++

        if not index.isValid():
            return False

        if role != Qt.EditRole:
            return False

        row = index.row()
        if row < 0 or row >= len(self._data.values):
            return False

        column = index.column()
        if column < 0 or column >= self._data.columns.size:
            return False

        self._data.values[row][column] = value

        self._data.values[row][1] = int(value)**2                             # +++
        self._data.values[row][2] = int(value)**3                             # +++

        self.dataChanged.emit(index, index)
        return True

    def dataChanged(self, index):
        row = index.row()
        col = index.column()

        print(f'Data has been changed on the row {row} and column {col}')


    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

    def flags(self, index):
        """Returns the flags used to describe the item.
        These determine whether the item can be checked, edited, and selected.
        ItemIsEditable: It can be edited.
        ItemIsEnabled: The user can interact with the item.
        ItemIsSelectable: It can be selected."""
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        self.model = PandasModel(df)
        self.table.setModel(self.model)

        self.table.resize(800, 600)
        self.setCentralWidget(self.table)




app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
