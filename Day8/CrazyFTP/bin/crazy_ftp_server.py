#!/usr/bin/env python3
__author__ = 'dmmjy9'

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from modules import main

if __name__ == '__main__':
    Entrypoint = main.ArgvHandler(sys.argv)