#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import subprocess

def list_dir(user_dir):
    command = 'ls -al ' + user_dir
    dir_list = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
    dir_list = bytes.decode(dir_list.stdout.read())
    return dir_list

def mkdir(user_dir,dir_name):
    new_dir = user_dir +'/' + dir_name
    command = 'mkdir ' + new_dir
    try:
        subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
        return 1
    except Exception:
        return 0