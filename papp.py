#!/usr/bin/python

import os
import subprocess
import sys
import zipfile

#functions
def CallSubProc(*args,**kwargs):
	retcode = subprocess.call(*args,**kwargs)
	if retcode != 0:
		print '@@@STEP_EXCEPTION@@@'
		sys.exit(1)


FILE_NAME = os.path.abspath(__file__)
DIR_NAME = os.path.dirname(FILE_NAME)
print sys.platform,__file__,FILE_NAME,DIR_NAME
print os.path.dirname(DIR_NAME)
print sys.executable

if sys.platform in ['win32','cygwin']:
	EXE_SUFFIX = '.exe'
else:
	EXE_SUFFIX = ''
JAVA_HOME = os.getenv('JAVA_HOME')
if JAVA_HOME:
	JAVA_EXEC = os.path.join(JAVA_HOME,'bin','java' + EXE_SUFFIX)	
	print JAVA_EXEC
	CallSubProc([JAVA_EXEC,'-version'])

with zipfile.ZipFile(sys.argv[1]) as zf:
	zf.printdir()
