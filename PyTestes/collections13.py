#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque

def search (lines, pattern, history=5):
	previous_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)	

#exemplo de uso de arquivo
if __name__ != '__name__':
	with open('somefile.txt') as f:
		for line, prevlines in search(f,'python',5):
			for pline in prevlines:
				print(pline, end='')
			print (line,end='')	
			print ('-'*20)
