#!/usr/bin/env python
from __future__ import print_function
import time
import sys
import math
import re

width = 50.0
usage = 'Usage: {} TIME\n\
    Where TIME can be expressed in a couple of ways\n\
    10      -> 10 seconds, just a number will be interpeted as seconds\n\
    10[MHS] -> for 10 minutes, hours or seconds\n\
    1:10    -> for 1 hour and 10 minutes\n\
    1:10:5  -> for 1 hour, 10 minutes and 5 seconds'.format(sys.argv[0])


def exitWith(message):
    print(message)
    print(usage)
    sys.exit(1)


def main():
    if len(sys.argv) > 2:
        exitWith('To many arguments')

    patterns = dict(mhs='^\d+:\d+:\d+$', mh='^\d+:\d+$', letter='^(\d)+([mhs])$')
    try:
        sleep = int(sys.argv[1])
    except ValueError:
            try:
                timestr = sys.argv[1]
                for name, pat in patterns.items():
                    m = re.match(pat, timestr, re.IGNORECASE)
                    if m:
                        if name == 'mhs':
                            hours, minutes, seconds = timestr.split(':')
                            sleep = 3600 * int(hours) + 60 * int(minutes) + int(seconds)
                            break
                        elif name == 'mh':
                            hours, minutes = timestr.split(':')
                            sleep = 3600 * int(hours) + 60 * int(minutes)
                            break
                        elif name == 'letter':
                            multiplydict = dict(s=1, m=60, h=3600)
                            sleep = int(m.group(1)) * multiplydict[m.group(2).lower()]
                            break
                else:
                    exitWith('Could not parse given time')
            except Exception:
                exitWith('Could not parse given time')
    except IndexError:
        exitWith('To few argumenst')

    sleep *= 5
    for i in xrange(sleep):
        nrstars = int(width / sleep * i)
        print('[{}{}]'.format('*' * nrstars, ' ' * int(math.ceil(width - nrstars))), end='\r')
        sys.stdout.flush()
        time.sleep(0.2)
    print('[{}]'.format('*' * int(width)))


if __name__ == '__main__':
    main()
