#!/usr/bin/env python3
__auther__ = 'dmmjy9'

class A:
	n = 'A'
	def f2(self):
		print("f2 from A")

class B(A):

	n = 'B'
	def f1(self):
		print("f1 from B")
	def f2(self):
		print("f2 from B")

class C(A):
	n = 'C'
	def f2(self):
		print("f2 from C")

class D(B,C):
	pass

d = D()
d.f2()