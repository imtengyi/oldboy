#!/usr/bin/env python3
__auther__ = 'dmmjy9'

class SchoolMember(object):
	def __init__(self,name,age,sex):
		self.name = name
		self.age  = age
		self.sex  = sex
	def enroll(self):
		print("SchoolMember [%s] is enrolled"%self.name)

class Teacher(SchoolMember):
	def __init__(self,name,age,sex,course,salary):
		super(Teacher,self).__init__(name,age,sex)
		self.course = course
		self.salary = salary
	def teaching(self):
		print("Teacher [%s] is teaching [%s]"%(self.name,self.course))

class Student(SchoolMember):
	member_nums = 0
	def __init__(self,name,age,sex,course,tution):
		super(Student,self).__init__(name,age,sex)
		self.course  = course
		self.tution = tution
	def pay_tution(self):
		print("Student [%s] paying tution [%s]"%(self.name,self.tution))
	def enroll(self):
		Student.member_nums += 1
		print("The [%s] school member [%s] is enrolled"%(Student.member_nums,self.name))


t1 = Teacher('Alex',22,'F','PY',1000)
t2 = Teacher('Tl',25,'M','PY',900)

s1 = Student('dmmjy9',22,'M','python',5000)
s2 = Student('dz',23,'F','python',15000)

t1.teaching()
s1.pay_tution()
s1.enroll()