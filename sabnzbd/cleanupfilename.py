#!/usr/bin/env python
from __future__ import print_function
import argparse
import re
import os
from path import Path


def main():
    parser = argparse.ArgumentParser(description='cleanup a filename, \
            replace . with spaces, delete some common shit at the end of a filename\
            ex: "actual.file.name-1080p.BluRay.x264-GECKOS[rarbg]" -> "actual filename"')
    parser.add_argument('filenames', nargs='+', help='list of files and folders to cleanup')
    args = parser.parse_args()
    for f in args.filenames:
        p = Path(f.strip())
        newname = rename(p.basename(), p.isdir())
        p = p.rename(Path.joinpath(p.dirname(), newname))
        print(p.abspath(), end='')


def rename(filename, dir):
    """Apply a series of regular expression on a filename to cleanup some clutter usualy added when
    downloading stuff from the internet.
    """
    suffixpatterns = ['x264', 'hdtv', '\d{3,4}p', '-', 'sample', 'nzb', 'par2', 'AAC', 'part\d{0,3}',
                      'DTS', 'subs', '5.1', 'BluRay', 'BARCODE', 'BDREmux', 'rar', 'nfo', 'WEB-DL',
                      'DD5', 'GECKOS', 'rarbg']
    extension = ''
    if dir:
        #  only remove these when it is directory
        suffixpatterns += ['mp4', 'mov', 'mwv', 'mpg']
    else:
        filename, extension = os.path.splitext(filename)
    compiled = [re.compile('\[?{}\]?.?$'.format(p), flags=re.IGNORECASE) for p in suffixpatterns]
    while True:
        for p in compiled:
            m = p.search(filename)
            if m:
                filename = p.sub('', filename)
                break
        else:
            break
    filename = re.sub('[._-]', ' ', filename)
    filename = filename.strip() + extension
    return filename


if __name__ == '__main__':
    main()
