#!/usr/bin/python

from subprocess import Popen, PIPE

client_sockets = []

ns = Popen(["netstat", "-an", "--unix"], stdout=PIPE)
output = ns.communicate()[0]
for line in output.split('\n'):
    if line.find("X11-unix") == -1 and len(line.split()) > 6 :
        inode = line.split()[6]
        client_sockets.append(inode)

lsof = Popen(["lsof", "-U", "+c0", "-w"], stdout=PIPE)
output = lsof.communicate()[0]
for line in output.split('\n'):
    try:
        inode = line.split()[7]
        if inode in client_sockets:
            print line
    except:
        pass
