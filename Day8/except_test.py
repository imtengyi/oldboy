#!/usr/bin/env python3
__author__ = 'dmmjy9'

class MumuException(Exception):
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return self.message
try:
    raise MumuException('My Exception')
except MumuException as e:
    print(e)