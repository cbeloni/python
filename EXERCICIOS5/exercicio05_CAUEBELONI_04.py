#!/usr/bin/python
#-*- coding: utf-8 -*-
count = 0
for i in range(18644,33087):
	if ('7' not in str(i)) and ('2' in str(i)):
		count += 1
print count		

	