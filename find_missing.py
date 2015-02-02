from path import Path
import argparse
import re
import sys

parser = argparse.ArgumentParser(description="find missing files in a series of numbered files")
parser.add_argument('--path', default='.', help='directory to look for the serie')
parser.add_argument('--file_pattern', help='file pattern to match files againts ex: *.txt, help_*')
parser.add_argument('--include_dirs', action='store_true', help='include directories in files to match')
args = parser.parse_args()

d = Path(args.path)
file_list = d.files(args.file_pattern)
if args.include_dirs:
	file_list += d.dirs()
serie = [int(re.search('\d+', f.name).group(0)) for f in file_list]
try:
	not_in_serie = [i for i in range(min(serie),max(serie)) if i not in serie]
except ValueError:
	sys.exit(0)

for i in not_in_serie:
	print '{} not in serie'.format(i)
