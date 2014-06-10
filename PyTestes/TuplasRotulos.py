#!/usr/bin/env python3
# -*- coding: utf-8 -*-
records = [
('foo',1,2),
('bar','hello'),
('foo',3,4),
]

for tag, *args in records:
	print (tag)