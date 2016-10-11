#!/usr/bin/env python3
# def calc(n):
#     print (n)
#     if n/2 > 1:
#         res = calc(n/2)
#         return res
# calc(100)

#Fibonacci
def fibonacci(arg1,arg2,stop_arg):
    if arg1 == 0:
        print(arg1,arg2)
    arg3 = arg1 + arg2
    print(arg3)
    if arg3 < stop_arg:
        fibonacci(arg2,arg3,stop_arg)
fibonacci(0,1,100)