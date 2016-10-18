#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import shelve

d = shelve.open('shelve_test')

class Test(object):
	def __init__(self,n):
		self.n = n

t1 = Test(123)
t2 = Test(123334)

name = ["alex","rain","test"]
d["test"] = name
d["t1"] = t1
d["t2"] = t2

d.close()