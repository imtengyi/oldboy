#!/usr/bin/env python3
__auther__ = 'dmmjy9'

class Animal:
	def __init__(self,name):
		self.name = name
	def talk(self):
		raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
	def talk(self):
		return "Cat_talk!"

class Dog(Animal):
	def talk(self):
		return "Dog_talk!"

animals = [Cat('Missy'),Dog('Lassie')]

for animal in animals:
	print(animal.name + ':' + animal.talk())