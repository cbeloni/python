#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
from collections import deque

q = deque(argv)
q.popleft()
q.append('argumento 2')

for i in q:
	print (i)