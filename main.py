"""
Problem 2 - Stone Mason Karel
Karel has been hired to build the columns in the Temple of Artemis in Efes.In particular, there are a set of arches where the stones (represented bybeepers, of course) are missing from the columns supporting the arches, asfollows:
When Karel is done, the missing columns should be replaced by beepers.

Karel may count on the following facts about the world, listed below:
• Karelstarts at bottom left corner, facing right (aka east)
• The columns areexactly four squares apart, on the 1st, 5th, 9th. and 13th columns.
• Karelcan assume that columns are always five units high. Your proaram will be mucheasier to write and easier to read.
if vou use for loops.
There are multipleopportunities to use for loops in this problem!
In addition to for loops, youshould be practicing defining functions.
For example, it would make sense tohave a build_column function.

"""
from stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    turn_left()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    move()
    move()
    move()
    turn_right()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    move()
    move()
    move()
    turn_left()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    move()
    move()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    turn_right()
    turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    run_karel_program()