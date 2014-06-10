#!/usr/bin/python3
# -*- coding: utf-8 -*-
def sum(items):
	head, *tail = items
	return head + sum(tail) if tail else head

items = [1,10,7,4,5,9]
print (sum(items))