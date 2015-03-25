#!/usr/bin/env python
from __future__ import print_function
import time
import sys
import math
import re

usage = 'Usage: {} TIME\n\
    Where TIME can be expressed in a couple of ways\n\
    10      -> 10 seconds, just a number will be interpeted as seconds\n\
    10[MHS] -> for 10 minutes, hours or seconds\n\
    1:10    -> for 1 hour and 10 minutes\n\
    1:10:5  -> for 1 hour, 10 minutes and 5 seconds'.format(sys.argv[0])

if len(sys.argv) > 2:
    print('To many arguments')
    print(usage)
    sys.exit(1)

width = 50.0
try:
    sleep = int(sys.argv[1])
except ValueError:
        timestr = sys.argv[1]
        if re.match('^\d+:\d+:\d+$', timestr):
            hours, minutes, seconds = timestr.split(':')
            sleep = 3600 * int(hours) + 60 * int(minutes) + int(seconds)
        elif re.match('^\d+:\d+$', timestr):
            hours, minutes = timestr.split(':')
            sleep = 3600 * int(hours) + 60 * int(minutes)
        elif re.match('^\d+[mhs]$', timestr, re.IGNORECASE):
            m = re.match('(\d+)([mhs])', timestr, re.IGNORECASE)
            multiplydict = dict(s=1, m=60, h=3600)
            sleep = int(m.group(1)) * multiplydict[m.group(2).lower()]
        else:
            print('Could not parse given time')
            print(usage)
            sys.exit(1)
except IndexError:
    print('To few argumenst')
    print(usage)
    sys.exit(1)

for i in xrange(sleep):
    nrstars = int(width / sleep * i)
    print('[{}{}]'.format('*' * nrstars, ' ' * int(math.ceil(width - nrstars))), end='\r')
    sys.stdout.flush()
    time.sleep(1)
