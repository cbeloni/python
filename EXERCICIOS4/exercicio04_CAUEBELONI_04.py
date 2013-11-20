#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
import random

texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''

texto = texto.replace('.', ' ')
texto = texto.replace(',', ' ')
texto = texto.lower()
lista = texto.split()
palavra = ''
listaPalavras = []
n = 0
qtd = len(lista)

for n in range(qtd):	
	palavra = lista[n]
	palavra1 = palavra[:1]
	palavra2 = palavra[len(palavra)-1:]	

	if palavra1 in 'python':
		listaPalavras.append(palavra)

print listaPalavras
