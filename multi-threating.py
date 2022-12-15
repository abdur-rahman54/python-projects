#!/bin/python

from multiprocessing import Process
import os
import time


def squar_number():
	for i in range(100):
		i * i
		time.sleep(0.1)

process = []
num_processes = os.cpu_count()

#create processes

for i in range (num_processes):
	p = Process(target = squar_number)
	process.append(p)
	
#start
for p in process:
	p.start()
	
#join
for p in process:
	p.join()
	
print ('end main')
