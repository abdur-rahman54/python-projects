#!/bin/python

from multiprocessing import Process
import os

process = []
num_processes = os.cpu_count()

#create processes

for i in range (num_process):
	p = Process
