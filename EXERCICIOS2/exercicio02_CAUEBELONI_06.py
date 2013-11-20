#!/usr/bin/python
#-*- coding: utf-8 -*-
print 'Calculos dos impostos sobre salario'
 
SALHORA = input("Entre com o valor de seu rendimento por hora: ")
HORAMES = input("Entre com a quantidade de horas trabalhdas no mês: ")
 
SALBRUTO = round(SALHORA*HORAMES,2)
IR = round(SALBRUTO * 0.11,2)
INSS = round(SALBRUTO * 0.08,2)
SIND = round(SALBRUTO * 0.05,2)
SALLIQ = round(SALBRUTO - (IR+INSS+SIND),2)
 
#print IR,INSS,SIND,SALLIQ
print ('\n+ Salario Bruto: %.2f reais.') % (SALBRUTO)
print ('- IR (11%): ')+ ('%.2f reais') % (IR)
print ('- INSS (8%): ')+('%.2f reais') % (INSS)
print ('- Sindicato (5%): ')+(' %.2f reais') % (SIND)
print ('= Salario Liquido:')+ (' %.2f reais') % (SALLIQ)