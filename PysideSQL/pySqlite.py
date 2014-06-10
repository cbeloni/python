#!/usr/bin/env python
import sqlite3
from PySide import QtCore, QtGui, QtSql

class EditableSqlModel(QtSql.QSqlQueryModel):
    def flags(self, index):
        flags = super(EditableSqlModel, self).flags(index)

        if index.column() in (1, 2):
            flags |= QtCore.Qt.ItemIsEditable

        return flags

    def setData(self, index, value, role):
        if index.column() not in (1, 2):
            return False

        primaryKeyIndex = self.index(index.row(), 0)
        id = self.data(primaryKeyIndex)

        self.clear()

        if index.column() == 1:
            ok = self.setFirstName(id, value)
        else:
            ok = self.setLastName(id, value)

        self.refresh()
        return ok

    def refresh(self):
        self.setQuery('select * from person')
        self.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
        self.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")

    def setFirstName(self, personId, firstName):
        query = QtSql.QSqlQuery()
        query.prepare('update person set firstname = ? where id = ?')
        query.addBindValue(firstName)
        query.addBindValue(personId)
        return query.exec_()

    def setLastName(self, personId, lastName):
        query = QtSql.QSqlQuery()
        query.prepare('update person set lastname = ? where id = ?')
        query.addBindValue(lastName)
        query.addBindValue(personId)
        return query.exec_()

def initializeModel(model):
    model.setQuery('select * from person order by id')
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")


offset = 0
views = []

def createView(title, model):
    global offset, views

    view = QtGui.QTableView()
    view.setGeometry(600,300,600,600)
    views.append(view)
    view.setModel(model)
    view.resizeColumnsToContents()
    view.sortByColumn(1,QtCore.Qt.DescendingOrder)
    view.setWindowTitle(title)
    view.move(300 + offset, 300 + offset)
    offset += 20
    view.show()


def abreConexao():
    ''' Abreconexao (nome do banco de dados sqlite)
    '''
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName('dados.db')
    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                QtGui.qApp.tr("Unable to establish a database connection.\n"
                              "This example needs SQLite support. Please read "
                              "the Qt SQL driver documentation for information "
                              "how to build it.\n\nClick Cancel to exit."),
                QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)
        return False
    
    query = QtSql.QSqlQuery()

    return True
      
if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    if not abreConexao():
        sys.exit(1)

    editableModel = EditableSqlModel()

    initializeModel(editableModel)

    createView("Editable Query Model", editableModel)

    sys.exit(app.exec_())        
        

