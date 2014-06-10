#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq

portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'aapl', 'shares': 50, 'price': 543.22},
{'name': 'sonda', 'shares': 200, 'price': 21.09},
{'name': 'YAHOO', 'shares': 35, 'price': 98.21},
{'name': 'gp', 'shares': 50, 'price': 72.33},
{'name': 'HP', 'shares': 69, 'price': 69.69},
]
cheap = heapq.nsmallest(3, portfolio,key=lambda s:s['price'])