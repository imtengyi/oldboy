#!/usr/bin/env python3
#coding:utf-8

name = input("Name:")
age = input("Age:")
job = input("Job:")

# print("Information of " + name + "\nName:" + name + "\nAge:" + age + "\nJob:" +job)
#
# print("Information of %s\nName:%s\nAge:%s\nJob:%s"%(name,name,age,job))

msg = '''
Information of %s
    Name:%s
    Age:%d
    Job:%s
'''%(name,name,int(age),job)
print (msg)