#!/bin/python

from threading import Thread
import os
import time


def squar_number():
	for i in range(100):
		i * i
		time.sleep(0.1)

threads = []
num_threads = 10

#create processes

for i in range (num_threads):
	t = Threads(target = squar_number)
	threads.append(p)
	
#start
for t in threads:
	t.start()
	
#join
for t in threads:
	t.join()
	
print ('end main')
