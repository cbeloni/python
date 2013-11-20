#!/usr/bin/python
#-*- coding: utf-8 -*-
import math

METROS = input("Entre com o tamanho em metros quadrados da área a ser pintada: ")
 
METROSLATAS = METROS / 3
if (METROSLATAS <=0):
 METROSLATAS = 1
  
QTDLATAS = math.floor(METROSLATAS / 18)
if (QTDLATAS<=0):
 QTDLATAS=1
  
PRECO = QTDLATAS * 80
 
 
#print IR,INSS,SIND,SALLIQ
print ('\n+ Quantidade de latas: %d latas. Preço total: %.2f reais') % (QTDLATAS,PRECO)