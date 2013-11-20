#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
import random

i=0
j=0
lista1 = []
lista2 = []
lista3 = []

for n in range(10):
	lista1.append(random.randint(1,100))

for n in range(10):
	lista2.append(random.randint(1,100))

for n in range(20):
	if (n % 2 == 0):
		lista3.append(lista1[i])
		i += 1
	else:
		lista3.append(lista2[j])
		j += 1

print lista1		
print lista2
print lista3