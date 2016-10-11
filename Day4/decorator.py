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

# def login(func):
#     def inner(arg):
#         print("Passed user verification.")
#         func(arg)
#     return inner
#
# @login
# def tv(name):
#     print("Welcome [%s] to TV page!"%name)
#
# tv('mumu')

def Before(request,kargs):
    print("Before")
def After(request,kargs):
    print("After")
def Filter(before_func,after_func):
    def outer(main_func):
        def wrapper(request,kargs):
            before_result = before_func(request,kargs)
            main_result = main_func(request,kargs)
            after_result = after_func(request,kargs)
        return wrapper
    return outer
@Filter(Before,After)
def index(request,kargs):
    print("index")