#!/usr/bin/env python3
__auther__ = 'dmmjy9'

class Animal:
	def __init__(self,name):
		self.name = name
	hobbies = 'meat'
	@classmethod		#类方法不能访问实例变量
	def talk(self):
		print("%s is talking"%self.hobbies)

	@staticmethod		#静态方法，不能访问类变量及实例变量
	def walk():
		print("%s is walking"%self.hobbies)

	@property			#把方法变成属性，可以访问类变量和实例变量
	def habit(self):
		print("%s's habit is xxoo"%self.name)

d = Animal("dmmjy9")
# d.talk()
Animal.talk()
# d.walk()
d.habit