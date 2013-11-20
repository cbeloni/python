#!/usr/bin/python
#-*- coding: utf-8 -*-
import random

min_valor = 100
max_valor = 0
for n in range(10):
	valor = random.randint(1, 100)
	if valor < min_valor:
		min_valor = valor
	if valor > max_valor:	
		max_valor = valor
	print 'o valor atual é %d o menor: %d e o maior: %d' % (valor,min_valor,max_valor)