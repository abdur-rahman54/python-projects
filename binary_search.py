#!/bin/python

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
