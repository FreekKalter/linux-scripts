from path import path
import os
import re

thisDir = path(os.getcwd())
archives = re.compile("part01\.rar$")

for f in thisDir.files():
    if( archives.search(f.name) ):
        if os.fork() == 0:
            os.execlp("unrar","unrar", "x", "-ad", f.abspath())
