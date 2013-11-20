#!/usr/bin/python
#-*- coding: utf-8 -*-
peso = input("Entre com o peso dos peixes: ")
excesso = peso - 40
 
 
if (excesso < 0):
 excesso *= (-1)
 
multa = excesso * 4
   
print 'Total de quilos pescados %.2f KG . Excesso %d. Multa %.2f reais. ' % (peso,excesso,multa)