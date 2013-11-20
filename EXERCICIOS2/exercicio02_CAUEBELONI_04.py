#!/usr/bin/python
#-*- coding: utf-8 -*-
v1 = input("Primeiro valor: ")
v2 = input("Segundo valor: ")
v3 = input("Terceiro valor: ")
if v1 > v2:
	maior = v1
else:
	maior = v2

if v3 > maior:
	maior = v3

print (maior)
 