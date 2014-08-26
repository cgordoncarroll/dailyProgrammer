Monty Hall Simulation
=====
The Monty Hall Problem is a probability puzzle that has a very non-intuitive answer for the average person. Here's the problem description taken from Wikipedia:
Suppose you're on a game show, and you're given the choice of three doors:
Behind one door is a car; behind the others, goats. You pick a door, say No.
1, and the host, who knows what's behind the doors, opens another door, say
No. 3, which has a goat. He then says to you, "Do you want to pick door No.
2?" Is it to your advantage to switch your choice?"
Formal Inputs & Outputs
===
Input Description
==
On standard console input, you will be given a single integer ranging
inclusively from 1 to 4,294,967,295 (unsigned 32-bit integer). This integer
is the number of times you should simulate the game for both tactics.
Remember that a single "game simulation" is your program randomly placing a
car behind one door and two goats behind the two remaining doors. You must
then randomly pick a door, have one of the two remaining doors open, but only
open if it's a goat behind said door! After that, if using the first tactic,
you may open the picked door, or if using the second tactic, you may open the
other remaining door. Keep track if your success rates in both simulations.
Output Description
==
On two seperate lines, print "Tactic 1: X% winning chance" and "Tactic 2: Y%
winning chance", where X and Y are the percentages of success for the
respective tactics
Sample Inputs & Outputs
===
Sample Input
==
1000000
Sample Output
==
Tactic 1: 33.3% winning chance
Tactic 2: 66.6% winning
