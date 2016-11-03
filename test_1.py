#!/usr/bin/env python3
__author__ = 'dmmjy9'

import threading,time

def light():
	if not event.isSet():
		event.set()
	count = 0
	while True:
		if count < 10:
			print("Green")
		elif count < 13:
			print("Yellow")
		elif count < 20:
			if event.isSet():
				event.clear()
			print("Red")
		else:
			event.set()
			count = 0
		time.sleep(1)
		count += 1
def car(n):
	while True:
		time.sleep(1)
		if event.isSet():
			print("car [%s] running"%n)
		else:
			print("car [%s] waiting"%n)
			event.wait()

if __name__ == '__main__':
	event = threading.Event()
	Light = threading.Thread(target=light)
	Light.start()
	for i in range(3):
		t = threading.Thread(target=car,args=(i,))
		t.start()