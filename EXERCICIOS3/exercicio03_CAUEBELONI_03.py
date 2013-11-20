#!/usr/bin/python
#-*- coding: utf-8 -*-
v_popa = 80000
v_popb = 200000
v_aperc = 3
v_bperc = 1.5
anos = 0
while v_popa < v_popb:
	 v_popa = int(v_popa + ((v_popa*v_aperc)/100))
	 v_popb = int(v_popb + ((v_popb*v_bperc)/100))
	 anos += 1	 
print "Para o país A ter a população maior será necessário %d anos." % (anos)