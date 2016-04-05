from path import Path
import os
import re
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dir', default='.', help='path to look for rar archives')
parser.add_argument('-t', '--to', default='.', help='path to extract content to')

args = parser.parse_args()
archive_dir = Path(os.getcwd())
archive_re = re.compile("(part01\.rar)|(r00)$")

for f in archive_dir.files():
    if(archive_re.search(f.name)):
        try:
            cp = subprocess.run(["unrar", "x", "-ad", f.abspath(), Path(args.to)], stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            print(cp.stderr)
