#!/usr/bin/python
#-*- coding: utf-8 -*-
lado1 = input("Primeiro lado: ")
lado2 = input("Segundo lado: ")
lado3 = input("Terceiro lado: ")

if lado1 == lado2 == lado3:
	print 'Triangulo equilátero.' 
elif (lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3):
	print 'Triangulo escaleno.' 
else:
	print 'Triângulo isósceles'
 