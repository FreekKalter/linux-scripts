#!/usr/bin/env python
from __future__ import print_function
import subprocess
import os
import sys
import re
import random
from path import path

standard_dir        = '/media/truecrypt4/down'
sock                = '/home/fkalter/.vlc-random.sock'
current_dir_file    = '/home/fkalter/.current_vlc_random'
log                 = '/home/fkalter/log.txt'

with open(current_dir_file, 'r') as f:
    current_dir = f.read()


def main():
    devnull = open(os.devnull, 'w')
    vlc_running = False
    try:
        if subprocess.check_call("echo 'logout' | nc -U {}".format(sock),
                                 shell=True, stdout=devnull, stderr=subprocess.STDOUT) == 0:
            vlc_running = True
    except:
        try:
            os.remove(sock)
        except:
            pass
        vlc_running = False

    if len(sys.argv) > 1:
        dir = sys.argv[1]
    else:
        if vlc_running:
            dir = current_dir
        else:
            dir = standard_dir

    dir = path(dir)
    random_movie = random.choice(dir.listdir())
    with open(log, 'a') as f:
        print(random_movie, file=f)

    if vlc_running:
        out = subprocess.check_output('echo add {}|nc -U {}'.format(random_movie, sock), shell=True)
        if re.search('menu select', out):
            subprocess.call('echo pause | nc -U {}'.format(sock), shell=True,
                            stdout=devnull, stderr=subprocess.STDOUT)
            subprocess.call('echo add {} | nc -U {}'.format(random_movie, sock), shell=True,
                            stdout=devnull, stderr=subprocess.STDOUT)
    else:
        subprocess.Popen(['vlc', '--extraintf', 'oldrc', '--rc-unix', sock, random_movie])

    with open(current_dir_file, 'w') as f:
        f.write(dir)


if __name__ == '__main__':
    main()
