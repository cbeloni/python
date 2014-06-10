#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *

class FrmCadDefault(Widget):
	"""docstring for ClassName"""
	def __init__(self, parent = None):
		super(FrmCadDefault, self).__init__(parent)
		self.FrmCadDefaultCreate()

	def FrmCadDefaultCreate(self):
		self.SetWindowTitle(u'Cadastro Padrão')		

		self.layoutPrincipal = LauoutVertical()

		self.txtCodigo = TextBox(self)

		self.ckAtivo = CheckBox ('Ativo', self)

		self.fLayout = FormLayout()

		hboxcodigo = LauoutHorizontal()

		self.fLayout.addRow('Código',hboxcodigo)




if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    client = FrmCadDefault()
    client.show()
    sys.exit(client.exec_())		
		