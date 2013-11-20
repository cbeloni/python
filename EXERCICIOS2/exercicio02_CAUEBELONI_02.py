#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
def ano_bissexto(ano):
	if (ano % 400) == 0:
		return True
	elif (ano % 100) == 0:
		return False
	elif (ano % 4) == 0:
		return True
	else:
		return False

ano = input("Insira o ano: ")

if ano_bissexto(ano):
	print 'Ano bissexto'
else:
	print 'Ano não é bissexto'