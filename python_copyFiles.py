import os
import shutil
import sys

def cpy(src,dst):
	shutil.copy(src,dst)

for filename in os.listdir(sys.argv[1]):
	cpy(sys.argv[1]+'/'+filename,sys.argv[2])



