#!/usr/bin/env python
from __future__ import print_function
import subprocess
import os
import re
import random
from path import path
import argparse

standard_dir        = '/media/truecrypt4/down'
sock                = '/home/fkalter/.vlc-random.sock'
current_dir_file    = '/home/fkalter/.current_vlc_random'
log                 = '/home/fkalter/log.txt'

with open(current_dir_file, 'r') as f:
    current_dir = f.read()


def main():
    parser = argparse.ArgumentParser(description='Play a random file in a given directory')
    parser.add_argument('directory', nargs='?', help='the directory to pick a file from')
    parser.add_argument('-d', '--delete', action='store_true',
                        help='delete the last picked file before picking a new one')
    args = parser.parse_args()

    if args.delete:
        with open('/home/fkalter/log.txt', 'r') as f:
            subprocess.call(['trash-put', reversed(f.readlines()).next().strip()])
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

    if args.directory:
        dir = args.directory
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
