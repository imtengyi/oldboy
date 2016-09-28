#!/usr/bin/env python3
# def login(func):
#     def inner():
#         print("Passed user verification.")
#         return func()
#     return inner
#
# @login
# def tv():
#     print("Welcome to TV page!")
#
# tv()

def login(func):
    def inner(arg):
        print("Passed user verification.")
        func(arg)
    return inner

@login
def tv(name):
    print("Welcome [%s] to TV page!"%name)

tv('mumu')