#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from datetime import date
def ano_bissexto(ano):
	if (ano % 400) == 0:
		return True
	elif (ano % 100) == 0:
		return False
	elif (ano % 4) == 0:
		return True
	else:
		return False

def quantidade_dias(anos):
	dias = 0 
	anoatual = (date.today().year)
	while anos > 0:		
		if ano_bissexto(anoatual):
			dias = dias + 366 
		else:
			dias = dias + 365 
		anos = anos - 1
		anoatual = anoatual - 1
	return dias

cigarros = input("Quantos cigarros você fuma por dia? ")         
anos = input("Quantos anos você já fumou? ")

diasFumando = quantidade_dias(anos)
minutosPerdido = cigarros * diasFumando * 10
diasPerdido = minutosPerdido / 60 / 24  

print 'dias de vida perdidos: %d ' % (diasPerdido)