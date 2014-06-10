#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyOrganize.ui'
#
# Created: Sun Jan 12 20:35:53 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtGui
import pyOrganizeGUI

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = pyOrganizeGUI.Ui_MainWindow()
        self.ui.setupUi(self)

app = QtGui.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
