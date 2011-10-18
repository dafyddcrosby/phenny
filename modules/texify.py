#!/usr/bin/env python
"""
texify.py - Phenny Texify Module

"""

import urllib

TEXIFY = '{nick}: http://texify.com/${tex}$'

def tex(phenny, input): 
   """Gives a link of rendered LaTeX"""
   query = input.group(2)
   if not query: 
      return phenny.reply('.tex what?')
   query = query.encode('utf-8')
   query = urllib.quote(query)

   output = TEXIFY.format(nick=input.nick, tex=query)
   phenny.say(output)
tex.commands = ['tex']
tex.priority = 'high'
tex.example = ".tex E=mc^2"



if __name__ == '__main__': 
   print __doc__.strip()
