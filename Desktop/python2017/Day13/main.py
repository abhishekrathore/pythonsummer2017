from library import sum,diff
import os
import shutil
import sys

print sum(4,5)
print diff(5,6)
print os.getcwd()

dest = sys.argv[1]
ext = sys.argv[2]

print sys.argv

if os.path.isdir(dest):
	print "is dir"
else:
	os.mkdir(dest)

for f in os.listdir("./"):
	if f[-len(ext):]==ext:
		shutil.copy("./"+f,"./"+dest)