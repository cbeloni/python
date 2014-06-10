#!/usr/bin/python3
# -*- coding: utf-8 -*-
def drop_first_last(grades):
	first, *middle, last = grades
	return avg(middle)

def avg(lista):
	return (sum(lista)/len(lista))

notas = [1,10,10,10,5]


print (drop_first_last(notas))
