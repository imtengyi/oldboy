#!/usr/bin/env python3
__author__ = 'dmmjy9'

from multiprocessing import Process
import os

def info(title):
	print(title)
	print('module name:',__name__)
	print('parent process:',os.getppid())
	print('process id:',os.getpid())
	print('\n\n')

def f(name):
	info('function')
	print('hello',name)

if __name__ == '__main__':
	info('main process line')
	p = Process(target=info,args=('bob',))
	p.start()
	p.join()