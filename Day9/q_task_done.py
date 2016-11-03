#!/usr/bin/env python3
__author__ = 'dmmjy9'

import threading,queue
import time
import random

def consumer(n):
	while True:
		print("consumer [%s] get task: %s"%(n,q.get()))
		time.sleep(1)
		q.task_done()	#send a single to producer after task finished

def producer(n):
	count = 1
	while True:
		time.sleep(random.randrange(3))
		if q.qsize() < 3:
			print("producer [%s] produced a new task: %s"%(n,count))
			q.put(count)
			count += 1
			q.join()	#queue is empty
			print("all task has been cosumed by consumers")

q = queue.Queue()

c1 = threading.Thread(target=consumer,args=(1,))
c2 = threading.Thread(target=consumer,args=(2,))
c3 = threading.Thread(target=consumer,args=(3,))

p1 = threading.Thread(target=producer,args=("p1",))
p2 = threading.Thread(target=producer,args=("p2",))
p3 = threading.Thread(target=producer,args=("p3",))
p4 = threading.Thread(target=producer,args=("p4",))



c1.start()
c2.start()
c3.start()
p1.start()
p2.start()
p3.start()
p4.start()