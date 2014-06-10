#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
d = deque(["A", "B", "C"])
d.append("D")

print ("Handling", d.popleft())