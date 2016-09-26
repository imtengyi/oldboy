#!/usr/bin/env python3

#one parameter
def show_1(a):
    print(a)
show_1(1)

#two parameters
def show_2(a,b):
    print(a)
    print(b)
show_2(1,2)

#defalut parameters
def show_3(a = 1):
    print(a)
show_3()

#dynamic parameter:*
def show_4(*arg):
    print(arg)
show_4(1,2,3)
#dynamic parameter:**
def show_5(**arg):
    print(arg)
show_5(k1='v1',k2='v2')
#dynamic parameter:both * and **
def show_6(*args,**kwargs):
    print(args)
    print(kwargs)
show_6(1,2,3,k1='v1',k2='v2')
#dynamic parameter:input list or dict
def show_7(*args,**kwargs):
    print(args)
    print(kwargs)
list_1 = [1,2,3]
dict_1 = {'k1':'v1','k2':'v2'}
show_7(list_1,dict_1)
show_7(*list_1,**dict_1)
#dynamic parameter:use list
str_1 = '{0} is {1} statement'
list_1 = ['This','a']
result_1 = str_1.format(*list_1)
print(result_1)
#dynamic parameter:use dict
str_2 = '{first} is {second} statement'
dict_2 = {'first':'This','second':'a'}
result_2 = str_2.format(**dict_2)
print(result_2)

#lambda
func = lambda a:a+1
result_3 = func(2)
print(result_3)