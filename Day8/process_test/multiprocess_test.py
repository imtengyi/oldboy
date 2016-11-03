#!/usr/bin/env python3
__author__ = 'dmmjy9'

from multiprocessing import Process
import time

def f(name):
	time.sleep(2)
	print('hello',name)
if __name__ == '__main__':
	p1 = Process(target=f,args=('bob',))
	p2 = Process(target=f,args=('bob',))
	p1.start()
	p2.start()
	p1.join()