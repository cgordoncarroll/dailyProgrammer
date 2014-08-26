#!/usr/bin/python

import sys

def makeTree(size, trunk, leaves):
	totalLevels = (size/2)+1 #since we know size is odd, we have to get the total number of levels (n + n-2 + n-4...)
	for i in xrange(1,size+1, 2):
		if totalLevels < 0:
			print i*leaves
		else:
			print ' ' * totalLevels + i*leaves
		totalLevels -= 1
	print ' '*(size/2) + trunk*3


makeTree(13, "=", "*")
makeTree(21, "#", "-")
