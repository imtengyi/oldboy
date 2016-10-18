#!/usr/bin/env python3
#coding:utf-8
__auther__ = 'dmmjy9'

import hashlib
m = hashlib.md5()
m.update(b"Hello")
m.update(b"It's me")
print(m.hexdigest())