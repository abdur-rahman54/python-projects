#!/bin/python

import random
import time

#Implementing binary search algorithm
#we will prove that binary search is faster than naive search
#naive search: scan entire list and ask if its equal to the target
#if yes, return the index
#if no, then return -1

def naive_search(l, target):
	for i in range (len(l)):
		if l[i] == target:
			return i
	return -1
	
#binary serach uses devide and conquer
#we will leverage the fact that our list is sorted

def binary_search (l, target, low = None, high = None):
	if low is None:
		low = 0
	if high is None:
		high = len(l) - 1
	
	if high < low:
		return -1


	midpoint = (low +  high) // 2
	
	if l [midpoint] == target:
		return midpoint
	elif target < l[midpoint]:
		return binary_search (l, target, low, midpoint-1)
	elif target > l [midpoint]:
		return binary_search (l, target, midpoint+1, high)
	else:
		return "Not Found"
	
if __name__ == '__main__':
	l = [1, 3, 5, 7, 10, 14]
	target = 7
	
	start = time.time()
	print (naive_search (l, target))
	end = time.time()
	print("Naive search took {} seconds.".format(end-start))
	
	start = time.time()
	print (binary_search (l, target))
	end = time.time()
	print("Binary search took {} seconds.\n".format(end-start))
	
	length = 10000
	#build a sorted list of length 10000
	sorted_list = set()
	while len(sorted_list) < length:
		sorted_list.add(random.randint(-3*length, 3*length))
	sorted_list = sorted (list(sorted_list))
	
	
	start = time.time()
	for target in sorted_list:
		naive_search(sorted_list, target)
	end = time.time()
	print("Naive search took {} seconds.".format(end-start))
	
	
	start = time.time()
	for target in sorted_list:
		binary_search(sorted_list, target)
	end = time.time()
	print("Binary search took {} seconds.".format(end-start))
	
