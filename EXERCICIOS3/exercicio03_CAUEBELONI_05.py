#!/usr/bin/python
#-*- coding: utf-8 -*-
a = input("Entre com o primeiro valor: ")
b = input("Entre com o segundo valor: ")

if b > a:
	dividendo = b
	divisor = a
else:
	dividendo = a
	divisor = b

while (dividendo % divisor) != 0 :
	c = dividendo % divisor
	dividendo = divisor
	divisor = c

print "MDC de %d e %d é igual a %d." % (a,b,divisor)
