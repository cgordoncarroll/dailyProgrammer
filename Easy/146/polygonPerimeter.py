#!/usr/bin/python

import sys,math

def main(argv):
    numSides = int(argv[0])
    circumradius = float(argv[1])

    oneSide = circumradius*(2*math.sin(math.pi/numSides))
    print str(round(oneSide*numSides, 3))
    if __name__ == "__main__":
        main(sys.argv[1:])
