#!/usr/bin/env python3
__author__ = 'dmmjy9'

import threading
import time

def sayhi(num):
	print("running on theard %s"%num)
	time.sleep(3)

if __name__ == '__main__':
	t_list = []
	for i in range (10):
		t = threading.Thread(target=sayhi,args=(i,))
		t.start()
		t_list.append(t)
	for i in t_list:
		i.join()
	print("---main---")