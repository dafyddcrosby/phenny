#!/usr/bin/env python
"""
russianroulette.py - Phenny Russian Roulette Module
Copyright (c) 2012 Dafydd Crosby - http://www.dafyddcrosby.com

Licensed under the Eiffel Forum License 2.
"""

import random
import time

def russianroulette(phenny, input): 
    phenny.say(input.nick + " puts the revolver to their head")
    time.sleep(2)
    chamber = random.randint(0, 5)
    if chamber == 5:
        phenny.say("BANG!")
        time.sleep(1)
        kill_msg = "dead on the floor"
        phenny.write(['KICK' + " " + input.sender + " " + input.nick + " " +
        kill_msg])
    else:
        phenny.say("click.")
    return

russianroulette.commands = ['russianroulette']

if __name__ == '__main__': 
   print __doc__.strip()
