#!/usr/bin/env python
from __future__ import print_function
import time
import sys
import math

width = 50.0
try:
    counter = int(sys.argv[1])
except ValueError:
    print('Use a integer value for counter')
    sys.exit(1)
except IndexError:
    print('Usage: {} counter\nwhere counter is a integer'.format(sys.argv[0]))
    sys.exit(1)

for i in xrange(counter):
    nrstars = int(width / counter * i)
    print('[{}{}]'.format('*' * nrstars, ' ' * int(math.ceil(width - nrstars))), end='\r')
    sys.stdout.flush()
    time.sleep(1)
