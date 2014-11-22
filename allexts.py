import sys
import os
rootpath=sys.argv[1]
allexts=set('')
for root, dirs, names in os.walk(rootpath):
	for name in names:
		ext = os.path.splitext(name)[1][1:]
		allexts.add(ext)
print(','.join(allexts))
