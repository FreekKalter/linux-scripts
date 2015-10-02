#!/usr/bin/env python
from __future__ import print_function
from path import Path
import sys
import subprocess
import re


for d in sys.argv[1:]:
    filename = re.sub('\.?(/Check me|pdf|rar)$', '', d) + ".cbr"
    dir = Path(d)
    jpgs = dir.files('*.jpg') + dir.files('*.jpeg')
    if len(jpgs) < 10:
        print('not enough jpges found to make a cbr: ' + d, file=sys.stderr)
        continue
    command = ['/usr/local/bin/rar', 'a', filename]
    try:
        subprocess.check_call(command + jpgs)
    except subprocess.CalledProcessError:
        print('"{}" returned non-zero exit status'.format(command), file=sys.stderr)
    print(d)
