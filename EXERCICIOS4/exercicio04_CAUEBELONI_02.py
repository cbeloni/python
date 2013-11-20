#!/usr/bin/python
#-*- coding: utf-8 -*-
import random

par = []
impar = []
valor = []

for n in range(20):
	valor.append(random.randint(1, 100))
	if (valor[n] % 2 == 0):
		par.append(valor[n])
	else:
		impar.append(valor[n])

#'o valor atual é %d o menor: %d e o maior: %d' %
print  'Valores ímpares:'
print  (impar)

print  'Valores pares:'
print  (par)

print 'Lista completa'
print (valor)