#!/usr/bin/env python3
__author__ = 'dmmjy9'

import threading
import time

def run(n):
	print("[%s]------running------\n"%n)
	time.sleep(2)
	print("[%s]------done------"%n)
def main():
	for i in range(5):
		t = threading.Thread(target=run,args=(i,))
		t.start()
		print("thread ",t.getName())

m = threading.Thread(target=main,args=())
m.setDaemon(True)
m.start()

print("main thread done")