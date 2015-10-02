#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import os
import re
import codecs
from path import Path


wordlist = []


def main():
    parser = argparse.ArgumentParser(description='rename dir based on files inside')
    parser.add_argument('dirname', help='path of directory to rename')
    args = parser.parse_args()
    p = Path(args.dirname)
    rename(p)


def rename(p):
    files = [f for f in p.walkfiles() if os.stat(f).st_size > 10 * 1024 * 1024]
    dirname = ''
    if is_gibberish(p.basename()):
        if len(files) == 1:
            dirname = files[0].basename().stripext()
        else:
            dirname = long_substr([f.namebase for f in files])
            pattern = re.compile('(scene|cd)$', re.IGNORECASE)
            dirname = pattern.sub('', dirname.strip())
        dirname = re.sub('[._]', ' ', dirname)
        dirname = re.sub('- ?$', '', dirname).strip()
        if dirname != '':
            # print(p.basename() + ' -> ' + dirname)
            p = p.rename(Path.joinpath(p.dirname(), dirname))
    print(p.abspath())


def is_gibberish(dir):
    for w in dir.split(' '):
        if w.upper() in wordlist:
            return False
    return True


def main_main():
    dirs = Path('/media/truecrypt4/down/').dirs()
    for d in dirs[0:1]:
        rename(Path(d))


def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0]) - i + 1):
                if j > len(substr) and all(data[0][i:i + j] in x for x in data):
                    substr = data[0][i:i + j]
    return substr

if __name__ == '__main__':
    with codecs.open('/usr/share/dict/american-english-large', mode='r', encoding='utf-8') as wl:
        wordlist = [word.strip().upper() for word in wl.readlines()]
    # print('done loading wordlist')
    main()
