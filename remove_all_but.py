#!/usr/bin/env python
from __future__ import print_function
from operator import attrgetter
from path import path
import time
import os
import sys
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Move oldest x files to trash")
    parser.add_argument("directory", help="the directory to cleanup")
    parser.add_argument("-a", "--all", action="store_true", help="same as 'ls -a', also consider .files")
    parser.add_argument("-k","--keep", required=True, type=int, help="number of files to keep")
    parser.add_argument("-t","--dry-run", help="only print files, no actual deleting is done", action="store_true")
    parser.add_argument("-p", "--permanent", action="store_true", help="delete permanently, default is to move files to trash")
    parser.add_argument("-v","--verbose", action="count", help="increase verbosity")
    args = parser.parse_args()

    if args.keep < 1:
        print("KEEP should be at least one, ohterwise just use 'rm *'")
        sys.exit(1)

    dir = path(args.directory)
    files = dir.files()
    if not args.all:
        # filter out files starting with a dot
        files = list(set(files) - set(dir.files('.*')))
    files = sorted(files, key=attrgetter('ctime'))

    if len(files) <= args.keep:
        print("nothing to be done")
        sys.exit(0)

    for f in files[:-args.keep]:
        try:
            if not args.dry_run:
                if args.permanent:
                    f.unlink()
                else:
                    subprocess.check_call(["trash", f.abspath()])
        except Exception as e:
            print("could not remove " + f, e)
        if args.verbose > 0 or args.dry_run:
            print(f.abspath())

if __name__ == "__main__":
    main()
