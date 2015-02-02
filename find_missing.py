from path import Path
import re

d = Path('.')
serie = [int(re.search('\d+', f.name).group(0))for f in d.files('*.txt')]
not_in_serie = [i for i in range(min(serie),max(serie)) if i not in serie]

for i in not_in_serie:
	print '{} not in serie'.format(i)
