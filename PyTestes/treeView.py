#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# données à représenter
my_array = [['Teste','01','02'],
            ['10','11','12'],
            ['20','21','22'],
            ['Novo Teste','21','22'],
            ['Novo 1','21','22'],
            ['Novo 2','21','22']]

def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setGeometry(1000,500,1000,500)
    w.show()
    sys.exit(app.exec_())

# création de la vue et du conteneur
class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        tablemodel = MyTableModel(my_array, self)
        tableview = QTableView()        
        botao1 = QPushButton()
        botao2 = QPushButton()
        tableview.setModel(tablemodel)
		

        layout = QVBoxLayout(self)
        layout.addWidget(tableview)
        layout.addWidget(botao1)
        layout.addWidget(botao2)
        self.setLayout(layout)

# création du modèle
class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent = None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return (self.arraydata[index.row()][index.column()])

    """
    def setData(self, index, value):
        self.arraydata[index.row()][index.column()] = value
        return True
    def flags(self, index):
        return Qt.ItemIsEditable
    """    

if __name__ == "__main__":
    main()
