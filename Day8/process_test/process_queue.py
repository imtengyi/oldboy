#!/usr/bin/env python3
__author__ = 'dmmjy9'

from multiprocessing import Process,Queue

def f(q):
	q.put([44,None,'hello'])

if __name__ == '__main__':
	q = Queue()
	p = Process(target=f,args=(q,))
	p.start()
	print("from parent:",q.get())
	p.join()