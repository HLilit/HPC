import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor


def cpy(src):
	shutil.copy(src,sys.argv[2])

def main():
	executor=ThreadPoolExecutor(len(os.listdir(sys.argv[1])))
	future = {executor.submit(cpy,sys.argv[1]+'/'+filename): filename for filename in os.listdir(sys.argv[1])}

if __name__=="__main__":
	main()


