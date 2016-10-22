#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import subprocess

obj = subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE)
obj_read = obj.stdout.read()
print(bytes.decode(obj_read))