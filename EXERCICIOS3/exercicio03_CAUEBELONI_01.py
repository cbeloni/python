#!/usr/bin/python
#-*- coding: utf-8 -*-
nota = input ("Entre com a nota de 0 à 10: ")
while nota not in [0,1,2,3,4,5,6,7,8,9,10]:
	print ('Valor incorreto')
	nota = input ("Entre com a nota de 0 à 10: ")
