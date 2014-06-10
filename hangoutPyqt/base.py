#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TextBox(QLineEdit):
	"""Caixa de texto"""
	def __init__(self, parent = None):
		super(TextBox, self).__init__(parent)

class Label(QLabel):
	"""Caixa de texto"""
	def __init__(self,pText = ' ', parent = None):
		super(Label, self).__init__(parent)
		self.setText(pText)

class CheckBox(QCheckBox):
	"""Caixa de texto"""
	def __init__(self,pText = ' ', parent = None):
		super(CheckBox, self).__init__(parent)
		self.setText(pText)

class Botao(QPushButton):
	"""Caixa de texto"""
	def __init__(self,pText = ' ', parent = None):
		super(Botao, self).__init__(parent)
		self.setText(pText)

class LayoutVertical(QVBoxLayout):
	"""Caixa de texto"""
	def __init__(self):
		super(LayoutVertical, self).__init__()		

class LayoutHorizontal(QVBoxLayout):
	"""Caixa de texto"""
	def __init__(self):
		super(LayoutVertical, self).__init__()	

class Widget(QWidget):
	def __init__(self):
		super(Widget, self).__init__()	


class FrmLayout(QFormLayout):
	"""docstring for ClassName"""
	def __init__(self):
		super(FrmLayout, self).__init__()
		