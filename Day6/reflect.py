#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import sys

class WebServer(object):
	def __init__(self,host,port):
		self.host = host
		self.port = port

	def start(self):
		print("Server is starting...")
	def stop(self):
		print("Server is stopping...")
	def restart(self):
		self.stop()
		self.start()

def test_run(ins,name):
	print("running:",name,ins.host)

if __name__ == '__main__':
	server = WebServer('localhost',333)
	print(sys.argv[1])
	if hasattr(server,sys.argv[1]):
		func = getattr(server,sys.argv[1])
		func()

	setattr(server,'run',test_run)
	server.run(server,'alex')