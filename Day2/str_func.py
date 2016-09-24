#!/usr/bin/env python3

# name = str("qwertyqwerty")
# print (type(str))
# print (dir(str))
#
# print(name.count("q"))
# print(name.center(50,'*'))
# print(name.capitalize())
# print(name.encode("gbk"))
# print(name.endswith("ty"))
# print(name.__contains__("er"))

def displayNumType(num):
    print (num, 'is',end='')
    if isinstance(num,(int, float, complex)):
        print ('a number of type:',type(num).__name__)
    else:
        print ('not a number at all.')

displayNumType(-69)
displayNumType(99999999999999999999999999999)
displayNumType(98.6)