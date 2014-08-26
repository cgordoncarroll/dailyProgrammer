#!/usr/bin/python

import sys

def main(argv):
	dialSize = int(argv[0])
	firstNum = int(argv[1])
	secondNum = int(argv[2])
	thirdNum = int(argv[3])

	totalIncrements = 0

	totalIncrements += dialSize*2 #First two full turns
	totalIncrements += firstNum #Turn to first num
	#Determine distance for turn 2
	secondTurn = (dialSize + firstNum - secondNum) % dialSize 
	if secondTurn == 0:
		secondTurn = dialSize
	totalIncrements += secondTurn

	#Another full rotation
	totalIncrements += dialSize
	#Determine distance for turn 3 starting at turn 2
	thirdTurn = (thirdNum - secondNum + dialSize) % dialSize
	if thirdTurn == 0:
		thirdTurn = dialSize
	totalIncrements += thirdTurn

	print totalIncrements

if __name__ == "__main__":
   main(sys.argv[1:])
