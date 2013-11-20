#!/usr/bin/python
#-*- coding: utf-8 -*-
v1 = input("Primeiro valor: ")
v2 = input("Segundo valor: ")
v3 = input("Terceiro valor: ")
if v1 > v2:
	v_maior = v1
else:
	v_maior = v2

if v3 > v_maior:
	v_maior = v3

if v1 < v2:
	v_menor = v1
else:
	v_menor = v2

if v3 < v_menor:
	v_menor = v3

print ('O menor valor: %d' % v_menor)
print ('O maior valor: %d' % v_maior)