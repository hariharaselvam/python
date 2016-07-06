import sys
if len(sys.argv)!=3:
	print "I need two file names"
	exit(1)
fin=file(sys.argv[1],"r")
fout=file(sys.argv[2],"w")
while True:
	line=fin.readline()
	if len(line)==0:break
	print line
	fout.write(line)
fin.close()
fout.close()
