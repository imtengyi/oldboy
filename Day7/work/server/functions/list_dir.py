#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import subprocess

def list_dir():
    dir_list = subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE)
    dir_list = bytes.decode(dir_list.stdout.read())
    return dir_list