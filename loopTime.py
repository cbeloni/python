#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

for i in range (0,4):
	for j in range(0,2):
		try:
			time.sleep(2)
			print "Teste " + str(i)
			break
		finally:
			print "Teste Final " + str(i)
	

