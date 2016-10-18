#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import shelve

test = shelve.open("shelve_test","rb")
a = test['test']
print(a)