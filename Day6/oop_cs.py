#!/usr/bin/env python3
__auther__ = 'dmmjy9'

class Role(object):
	ac = None
	def __init__(self,name,role,weapon,life_value):
		self.name = name
		self.role = role
		self.weapon = role
		self.life_val = life_value

	def buy_weapon(self,weapon):
		print("%s is buying [%s]"%(self.name,weapon))
		self.weapon = weapon


p1 = Role('police_1','Police','B10',90)
t1 = Role('terrorist_1','Terrorist','B11',100)
p1.buy_weapon('AK47')
t1.buy_weapon('B51')

print("P1:",p1.weapon,t1.ac)
print("T1:",t1.weapon,t1.ac)