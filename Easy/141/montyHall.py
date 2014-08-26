#! /bin/python
import random
input = int(9999)
switch = 0
stay = 0
doors = [0,1,2]
for x in xrange(input):
    prize = random.choice(doors)
    picked = random.choice(doors)
    goats = set(doors) - set([prize])
    remaining = set(doors) - set([picked])
    opened = random.choice(list(goats.intersection(remaining)))
    if picked == prize:
        stay = stay + 1
    newpick = (set(doors) - set([picked]) - set([opened])).pop()
    if newpick == prize:
        switch = switch + 1
print "stay: " + str((stay / float(input) * 100.0)) + "%"
print "switch: " + str((switch / float(input) * 100.0)) + "%"
