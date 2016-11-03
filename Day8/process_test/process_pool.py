#!/usr/bin/env python3
__author__ = 'dmmjy9'

from multiprocessing import Process,Pool,freeze_support
import time

def Foo(i):
	time.sleep(2)
	return i+100
def Bar(arg):
	print('-->exec done:',arg)


if __name__ == '__main__':
	freeze_support()
	pool = Pool(5)		#setup a pool that allow 5 threads at the same time
	for i in range(10):
		pool.apply_async(func=Foo,args=(i,),callback=Bar)	#cannot use 'callback' when sync
		# pool.apply(func=Foo,args=(i,))

	print('end')
	pool.close()
	pool.join()			#shutdown program when process in pool finished.