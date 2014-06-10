#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui




if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    layout = QtGui.QGridLayout()

    model = QtGui.QStandardItemModel(4, 2)
    Button = QtGui.QPushButton("OK")
    #absModel = QtCore.QAbstractItemModel()
    selectionModel = QtGui.QItemSelectionModel(model) 
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "Nome")
    #model.setStringList(list)

    tableView = QtGui.QTableView()
    layout.addWidget(tableView, 0, 0, 1, 1)
    layout.addWidget(Button, 0, 1, 1, 1)
    setLayout(layout)
    tableView.setModel(model)

    #for row in range(4):
    #    for column in range(2):
    #        index = model.index(row, column, QtCore.QModelIndex())
    #        model.setData(index, (row + 10) * (column + 1))
    
    tableView.setSortingEnabled(1)
    tableView.resizeRowToContents(9)
    #main = QtGui.QMainWindow()
    
    tableView.setWindowTitle("Spin Box Delegate")
    tableView.show()
    
    #main.show()
    sys.exit(app.exec_())

