#!/usr/bin/env python3
__author__ = 'dmmjy9'

from multiprocessing import Process,Pipe

def f(conn):
	conn.send([42,None,'hello'])		#send data to pipe
	conn.close()

if __name__ == '__main__':
	parent_conn,child_conn = Pipe()			#create pipe object
	p = Process(target=f,args=(child_conn,))
	p.start()
	print(parent_conn.recv())	#get data from pipe
	p.join()