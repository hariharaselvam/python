import re
import sys
count=len(sys.argv)
if len(sys.argv)<3:
	print "The program needs atleast 3 inputs"
	exit(1)
n=count-1;
outfile=sys.argv[n];


fout=file(outfile,"w")


for i in range(1,n):
	filename=sys.argv[i]
	fin=file(filename,"r")
	data=fin.read()
	
	print filename
	fout.write(data)
	fin.close()
fout.close()
