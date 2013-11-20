#!/usr/bin/python
#-*- coding: utf-8 -*-
fibonacci =  []
fibonacci.append(1)
fibonacci.append(1)

k = 2
loops = input("Qual o número de Fibonacci desejado? ")
while k <= loops-1:
	 n = fibonacci[k-1] + fibonacci[k-2] 
	 fibonacci.append(n)
	 k += 1	 
print "O valor de Fibonacci é %d." % (fibonacci[k-1])